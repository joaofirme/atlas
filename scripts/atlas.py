"""Catálogos e consulta read-only do Atlas. Não executa consultas em dados."""
import argparse
import json
import re
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = ('metrics', 'technical', 'dimensions', 'datasets', 'ontology',
           'business_rules', 'data_products', 'skills')
INDEX_TYPES = {'metric': 'metrics.json', 'dimension': 'dimensions.json',
               'dataset': 'datasets.json', 'concept': 'concepts.json',
               'business_rule': 'business_rules.json', 'analysis_skill': 'skills.json'}
REFERENCE_FIELDS = {'dimensions', 'relationships', 'business_rules', 'datasets',
                    'related_objects', 'compatible_metrics', 'recommended_for',
                    'not_recommended_for', 'metrics', 'rules', 'concepts', 'skills',
                    'entity', 'entities', 'superseded_by'}


def objects():
    result = {}
    for folder in FOLDERS:
        base = ROOT / folder
        if not base.exists():
            continue
        for path in sorted(base.rglob('*')):
            if path.suffix not in ('.yaml', '.yml', '.md') and path.name != 'SKILL.md':
                continue
            text = path.read_text(encoding='utf-8')
            if path.suffix == '.md' or path.name == 'SKILL.md':
                if not text.startswith('---\n'):
                    continue
                text = text.split('---', 2)[1]
            loaded = yaml.safe_load(text) or {}
            obj = loaded.get('metadata', loaded)
            if not isinstance(obj, dict) or 'id' not in obj:
                continue
            if obj['id'] in result:
                raise ValueError('ID duplicado: ' + obj['id'])
            result[obj['id']] = {**obj,
                'evidence_status': obj.get('evidence_status', 'observed'),
                'path': path.relative_to(ROOT).as_posix()}
    return result


def normalize(value):
    value = unicodedata.normalize('NFKD', str(value).lower())
    return re.sub(r'[^a-z0-9]+', ' ', ''.join(c for c in value if not unicodedata.combining(c))).strip()


def dependencies(obj):
    return (obj.get('formula') or {}).get('dependencies') or []


def closure(identifier, catalog):
    found = set()
    def visit(key):
        for dep in dependencies(catalog[key]):
            if dep not in found:
                found.add(dep)
                visit(dep)
    visit(identifier)
    return found


def entry(obj):
    return dict(id=obj['id'], title=obj['title'], type=obj['type'], domain=obj['domain'],
                synonyms=obj.get('synonyms') or [], questions=obj.get('business_questions') or [],
                status=obj['status'], evidence_status=obj['evidence_status'], path=obj['path'])


def index(catalog, object_type='metric'):
    return [entry(o) for o in catalog.values() if o['type'] == object_type
            and (object_type != 'metric' or o.get('kind') == 'indicador')]


def search(query, entries, limit=5, certified_only=False):
    words = set(normalize(query).split()) - {'a', 'o', 'as', 'os', 'de', 'da', 'do', 'em', 'quanto', 'qual', 'que', 'estao'}
    ranked = []
    for item in entries:
        if certified_only and item['status'] != 'certified':
            continue
        labels = [item['id'], item['title'], *item.get('synonyms', []), *item.get('questions', [])]
        score = max((len(words & set(normalize(label).split())) / max(len(words), 1)
                     + (2 if normalize(query) == normalize(label) else 0) for label in labels), default=0)
        if score:
            ranked.append((score, item))
    return [{**item, 'score': round(score, 3)} for score, item in
            sorted(ranked, key=lambda pair: (-pair[0], pair[1]['id']))[:limit]]


def search_all(query, catalog, object_types=None, limit=10, certified_only=False):
    types = object_types or tuple(INDEX_TYPES)
    return search(query, [item for kind in types for item in index(catalog, kind)],
                  limit, certified_only)


def public_object(identifier, catalog):
    if identifier not in catalog:
        raise KeyError(f'Objeto não encontrado: {identifier}')
    obj = dict(catalog[identifier])
    obj['authority'] = ('official' if obj['status'] == 'certified' and
                        obj['evidence_status'] == 'certified' else 'observed_not_official')
    return obj


def _ids(value):
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [v if isinstance(v, str) else v.get('id') or v.get('dimension') for v in value]
    if isinstance(value, dict):
        return [item for nested in value.values() for item in _ids(nested) if item]
    return []


def context(identifier, catalog):
    obj = catalog[identifier]
    chain = {identifier} | closure(identifier, catalog)
    tables = {t['table'] for key in chain for t in catalog[key].get('dependency_table_sources', [])}
    relations = [o for o in catalog.values() if o['type'] == 'relationship'
                 and any(str(o.get('from_object', '')).startswith(t + '.') for t in tables)]
    related_tables = tables | {o['to_object'].split('.')[0] for o in relations}
    dims = [o for o in catalog.values() if o['type'] == 'dimension'
            and (o.get('physical_mapping') or {}).get('semantic_table') in related_tables]
    impacts = [key for key in catalog if catalog[key]['type'] == 'metric'
               and key != identifier and identifier in closure(key, catalog)]
    pages_path = ROOT / 'docs/ingestoes/2026-09-06-modelo-corporativo/uso_no_relatorio.json'
    pages = json.loads(pages_path.read_text(encoding='utf-8')) if pages_path.exists() else []
    names = {s for key in [identifier, *impacts] for s in catalog[key].get('synonyms', [])}
    uses = []
    for page in pages:
        for visual in page['visuals']:
            refs = sorted({r['property'] for r in visual['refs'] if r['kind'] == 'Measure' and r['property'] in names})
            if refs:
                uses.append(dict(page=page['title'], visibility=page['visibility'], measures=refs,
                                  source=visual['source'], note='Referência observada; verificar filtros.'))
    ref = lambda key: {'id': key, 'path': catalog[key]['path']}
    guidance = [ref(key) for key, item in catalog.items()
                if item['type'] in ('analysis_skill', 'business_rule', 'concept')
                and identifier in (ROOT / item['path']).read_text(encoding='utf-8')]
    return dict(metric=public_object(identifier, catalog),
                dependencies=[ref(k) for k in sorted(chain - {identifier})],
                impacts=[ref(k) for k in sorted(impacts)],
                candidate_dimensions=[ref(o['id']) for o in dims],
                linked_dimensions=[ref(k) for k in _ids(obj.get('dimensions')) if k in catalog],
                dimension_compatibility_status=obj.get('dimension_compatibility_status', 'not_declared'),
                datasets=[ref(k) for k in _ids(obj.get('datasets')) if k in catalog],
                business_rules=[ref(k) for k in _ids(obj.get('business_rules')) if k in catalog],
                observed_relationships=[ref(o['id']) for o in relations], report_usage=uses,
                analysis_guidance=guidance,
                limitations='Objetos observed/draft não são verdade oficial. O Atlas não executa DAX, SQL ou acessa valores atuais.')


def _references(obj):
    refs = set(dependencies(obj))
    for field in REFERENCE_FIELDS:
        refs.update(_ids(obj.get(field)))
    return refs


def _present(value):
    return value is not None and value != '' and value != [] and value != {}


def _validate_certified(obj):
    common = ['title', 'domain', 'version', 'definition', 'sources', 'validation']
    required = {
        'metric': ['unit', 'grain', 'dimensions', 'datasets', 'business_rules', 'data_sources'],
        'dimension': ['entity', 'key', 'physical_mapping', 'compatible_metrics'],
        'dataset': ['business_description', 'grain', 'dimensions', 'physical', 'lineage']}
    missing = [field for field in common + required.get(obj['type'], []) if not _present(obj.get(field))]
    owners = obj.get('owners') or {}
    for field in ('business', 'technical'):
        if not owners.get(field):
            missing.append('owners.' + field)
    validation = obj.get('validation') or {}
    for field in ('reviewed_by', 'reviewed_at', 'evidence'):
        if not _present(validation.get(field)):
            missing.append('validation.' + field)
    if obj.get('evidence_status') != 'certified':
        missing.append('evidence_status=certified')
    if missing:
        raise ValueError(f"{obj['id']}: certified incompleto: {', '.join(sorted(set(missing)))}")


def validate(catalog):
    allowed_status = {'draft', 'in_review', 'certified', 'deprecated'}
    allowed_evidence = {'observed', 'proposed', 'certified'}
    for obj in catalog.values():
        if obj.get('status') not in allowed_status:
            raise ValueError(f"{obj['id']}: status inválido")
        if obj.get('evidence_status') not in allowed_evidence:
            raise ValueError(f"{obj['id']}: evidence_status inválido")
        if obj.get('status') == 'certified':
            _validate_certified(obj)
        for key in _references(obj):
            if key and key not in catalog:
                raise ValueError(f"{obj['id']}: referência ausente {key}")
    visiting, done = set(), set()
    def visit(key):
        if key in visiting:
            raise ValueError('Ciclo de métricas: ' + key)
        if key in done:
            return
        visiting.add(key)
        for dep in dependencies(catalog[key]):
            visit(dep)
        visiting.remove(key)
        done.add(key)
    for key in catalog:
        visit(key)
    labels = {}
    for obj in catalog.values():
        if obj['status'] == 'deprecated':
            continue
        for label in [obj['title'], *(obj.get('synonyms') or [])]:
            normalized = normalize(label)
            if normalized in labels and obj['status'] == 'certified' and catalog[labels[normalized]]['status'] == 'certified':
                raise ValueError(f"Conflito de nome certificado: {labels[normalized]} e {obj['id']} ({label})")
            labels[normalized] = obj['id']


def build(catalog):
    target = ROOT / 'catalog'
    target.mkdir(exist_ok=True)
    for kind, filename in INDEX_TYPES.items():
        (target / filename).write_text(json.dumps(index(catalog, kind), ensure_ascii=False,
                                                   separators=(',', ':')) + '\n', encoding='utf-8')
    groups = {'catalogo': [], 'catalogo-tecnico': []}
    for obj in catalog.values():
        group = 'catalogo-tecnico' if obj['path'].startswith(('technical/', 'data_products/')) else 'catalogo'
        groups[group].append(obj)
    for name, entries in groups.items():
        lines = ['# ' + ('Catálogo de negócio' if name == 'catalogo' else 'Inventário técnico'), '',
                 'Gerado por `python scripts/atlas.py build`. Todos os estados vêm dos contratos.', '',
                 '[Consulta curta](consulta.md) · [Negócio](catalogo.md) · [Técnico](catalogo-tecnico.md)', '',
                 '| ID | Nome | Tipo | Domínio | Status | Evidência |', '|---|---|---|---|---|---|']
        if name == 'catalogo-tecnico':
            lines.insert(4, 'Os objetos `tabela_*` preservam a carga técnica original e não comprovam produto governado.\n')
        for obj in entries:
            lines.append(f"| [{obj['id']}](<../{obj['path']}>) | {obj['title']} | {obj['type']} | {obj['domain']} | {obj['status']} | {obj['evidence_status']} |")
        (ROOT / 'docs' / (name + '.md')).write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['search', 'show', 'build', 'validate'])
    parser.add_argument('query', nargs='?')
    parser.add_argument('--type', dest='object_types', action='append', choices=tuple(INDEX_TYPES))
    parser.add_argument('--certified-only', action='store_true')
    args = parser.parse_args()
    catalog = objects()
    validate(catalog)
    if args.command == 'build':
        build(catalog)
    elif args.command == 'validate':
        print(f'{len(catalog)} objetos; governança, referências, conflitos e ciclos verificados.')
    elif args.command == 'search':
        print(json.dumps(search_all(args.query or '', catalog, args.object_types, 10,
                                    args.certified_only), ensure_ascii=False, indent=2))
    else:
        if args.query not in catalog:
            parser.error('ID não encontrado')
        result = context(args.query, catalog) if catalog[args.query]['type'] == 'metric' else public_object(args.query, catalog)
        print(json.dumps(result, ensure_ascii=False, indent=2, default=str))


if __name__ == '__main__':
    main()
