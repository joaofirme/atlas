"""Busca, validação e índices do Atlas/Alexandria. Não executa consultas aos dados da Farmax."""
import argparse
import json
import re
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = ('metrics', 'technical', 'dimensions', 'ontology', 'business_rules', 'datasets', 'data_products', 'skills')
STOPWORDS = {'a', 'o', 'as', 'os', 'de', 'da', 'do', 'em', 'quanto', 'qual', 'que', 'estao', 'para', 'por', 'um', 'uma'}
CATALOG_FILES = {
    'metric': 'metrics.json',
    'dimension': 'dimensions.json',
    'dataset': 'datasets.json',
    'concept': 'concepts.json',
    'business_rule': 'business_rules.json',
    'analysis_skill': 'skills.json',
}


def objects():
    result = {}
    for folder in FOLDERS:
        base = ROOT / folder
        if not base.exists():
            continue
        for path in sorted(base.rglob('*')):
            if path.suffix not in ('.yaml', '.md'):
                continue
            text = path.read_text(encoding='utf-8')
            if path.suffix == '.md':
                if not text.startswith('---\n'):
                    continue
                text = text.split('---', 2)[1]
            obj = yaml.safe_load(text)
            if not isinstance(obj, dict):
                continue
            obj = obj.get('metadata', obj)
            if not isinstance(obj, dict) or 'id' not in obj:
                continue
            if obj['id'] in result:
                raise ValueError('ID duplicado: ' + obj['id'])
            result[obj['id']] = {**obj, 'path': path.relative_to(ROOT).as_posix()}
    return result


def normalize(value):
    value = unicodedata.normalize('NFKD', str(value or '').lower())
    return re.sub(r'[^a-z0-9]+', ' ', ''.join(c for c in value if not unicodedata.combining(c))).strip()


def governance_state(obj):
    governance = obj.get('governance') or {}
    evidence_level = governance.get('evidence_level')
    if evidence_level:
        return evidence_level
    if obj.get('status') == 'certified':
        return 'certified'
    if obj.get('status') == 'in_review':
        return 'reviewed'
    return 'observed'


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


def _list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def dimension_ids(obj):
    value = obj.get('dimensions')
    if isinstance(value, list):
        return value
    if isinstance(value, dict):
        return _list(value.get('allowed'))
    return []


def rule_ids(obj):
    value = obj.get('business_rules')
    if isinstance(value, dict):
        return _list(value.get('required')) + _list(value.get('optional'))
    return _list(value)


def dataset_ids(obj):
    value = obj.get('datasets')
    if isinstance(value, dict):
        return _list(value.get('recommended')) + _list(value.get('supported'))
    return _list(value)


def public_entry(obj):
    return {
        'id': obj['id'],
        'title': obj.get('title', obj['id']),
        'type': normalized_type(obj),
        'domain': obj.get('domain'),
        'status': obj.get('status'),
        'governance_state': governance_state(obj),
        'synonyms': obj.get('synonyms') or [],
        'questions': obj.get('business_questions') or [],
        'path': obj['path'],
        'legacy': obj.get('type') == 'data_product' and obj['path'].startswith('data_products/'),
    }


def normalized_type(obj):
    if obj.get('type') == 'data_product' and obj['path'].startswith('data_products/'):
        return 'dataset'
    return obj.get('type')


def index(catalog):
    """Compatibilidade: índice de métricas de negócio."""
    return [public_entry(o) for o in catalog.values()
            if o['path'].startswith('metrics/') and o.get('kind') == 'indicador']


def type_index(catalog, object_type):
    entries = [public_entry(o) for o in catalog.values() if normalized_type(o) == object_type]
    return sorted(entries, key=lambda e: (e['domain'] or '', e['title'], e['id']))


def all_index(catalog):
    supported = set(CATALOG_FILES)
    entries = [public_entry(o) for o in catalog.values() if normalized_type(o) in supported]
    return sorted(entries, key=lambda e: (e['type'] or '', e['domain'] or '', e['title'], e['id']))


def search(query, entries, limit=5):
    words = set(normalize(query).split()) - STOPWORDS
    ranked = []
    for entry in entries:
        labels = [entry['id'], entry['title'], *entry.get('synonyms', []), *entry.get('questions', [])]
        score = max((len(words & set(normalize(s).split())) / max(len(words), 1)
                     + (2 if normalize(query) == normalize(s) else 0) for s in labels), default=0)
        if score:
            ranked.append((score, entry))
    return [{**entry, 'score': round(score, 3)} for score, entry in
            sorted(ranked, key=lambda pair: (-pair[0], pair[1]['id']))[:limit]]


def search_all(query, catalog, object_type=None, limit=5):
    entries = type_index(catalog, object_type) if object_type else all_index(catalog)
    return search(query, entries, limit=limit)


def context(identifier, catalog):
    obj = catalog[identifier]
    chain = {identifier} | closure(identifier, catalog)
    tables = {t['table'] for key in chain for t in catalog[key].get('dependency_table_sources', []) if isinstance(t, dict) and t.get('table')}
    relations = [o for o in catalog.values() if o.get('type') == 'relationship'
                 and any(str(o.get('from_object', '')).startswith(t + '.') for t in tables)]
    related_tables = tables | {o['to_object'].split('.')[0] for o in relations if o.get('to_object')}
    explicit_dims = [catalog[k] for k in dimension_ids(obj) if k in catalog]
    inferred_dims = [o for o in catalog.values() if o.get('type') == 'dimension'
                     and (o.get('physical_mapping') or {}).get('semantic_table') in related_tables]
    dims_by_id = {o['id']: o for o in [*explicit_dims, *inferred_dims]}
    impacts = [key for key in catalog if catalog[key].get('type') == 'metric'
               and key != identifier and identifier in closure(key, catalog)]
    pages_path = ROOT / 'docs/ingestoes/2026-09-06-modelo-corporativo/uso_no_relatorio.json'
    uses = []
    if pages_path.exists():
        pages = json.loads(pages_path.read_text(encoding='utf-8'))
        names = {s for key in [identifier, *impacts] for s in catalog[key].get('synonyms', [])}
        for page in pages:
            for visual in page['visuals']:
                refs = sorted({r['property'] for r in visual['refs'] if r['kind'] == 'Measure' and r['property'] in names})
                if refs:
                    uses.append(dict(page=page['title'], visibility=page['visibility'], measures=refs,
                                     source=visual['source'], note='Referência direta ou dependência transitiva; verificar filtros e ramos condicionais no visual.'))
    ref = lambda key: {'id': key, 'path': catalog[key]['path'], 'status': catalog[key].get('status'),
                       'governance_state': governance_state(catalog[key])}
    guidance = [ref(key) for key, item in catalog.items()
                if item.get('type') in ('analysis_skill', 'business_rule', 'concept')
                and identifier in (ROOT / item['path']).read_text(encoding='utf-8')]
    datasets = [ref(k) for k in dataset_ids(obj) if k in catalog]
    rules = [ref(k) for k in rule_ids(obj) if k in catalog]
    return dict(metric=obj, governance_state=governance_state(obj),
                dependencies=[ref(k) for k in sorted(chain - {identifier})],
                impacts=[ref(k) for k in sorted(impacts)],
                dimensions=[ref(k) for k in sorted(dims_by_id)],
                datasets=datasets, business_rules=rules,
                observed_relationships=[ref(o['id']) for o in relations], report_usage=uses,
                analysis_guidance=guidance,
                limitations='Objetos observados ou em rascunho não são regras oficiais. Sem dados atuais ou execução DAX/SQL. Abrir apenas as referências necessárias.')


def get_object(identifier, catalog, expected_type=None):
    if identifier not in catalog:
        raise KeyError(identifier)
    obj = catalog[identifier]
    obj_type = normalized_type(obj)
    if expected_type and obj_type != expected_type:
        raise ValueError(f'{identifier} é {obj_type}, não {expected_type}')
    return {**obj, 'normalized_type': obj_type, 'governance_state': governance_state(obj)}


def _require(obj, fields):
    missing = []
    for field in fields:
        value = obj.get(field)
        if value is None or value == '' or value == [] or value == {}:
            missing.append(field)
    return missing


def _validate_certified(obj):
    if obj.get('status') != 'certified':
        return
    owners = obj.get('owners') or {}
    missing = _require(obj, ['title', 'domain', 'sources', 'validation'])
    if not owners.get('business'):
        missing.append('owners.business')
    if not owners.get('technical'):
        missing.append('owners.technical')
    validation = obj.get('validation') or {}
    if not validation.get('reviewed_by') or not validation.get('reviewed_at') or not validation.get('evidence'):
        missing.append('validation.review/evidence')
    governance = obj.get('governance') or {}
    if governance.get('evidence_level') != 'certified' or governance.get('source_of_truth') is not True:
        missing.append('governance(certified/source_of_truth)')
    obj_type = normalized_type(obj)
    type_fields = {
        'metric': ['definition', 'unit', 'grain', 'formula', 'dimensions'],
        'dimension': ['definition', 'entity'],
        'dataset': ['definition'],
        'concept': ['definition'],
        'business_rule': ['definition'],
        'analysis_skill': [],
    }
    missing.extend(_require(obj, type_fields.get(obj_type, [])))
    if missing:
        raise ValueError(f"{obj['id']}: certificado incompleto: {', '.join(sorted(set(missing)))}")


def _validate_references(obj, catalog):
    refs = []
    refs.extend((x, 'formula.dependencies') for x in dependencies(obj))
    refs.extend((x, 'dimensions') for x in dimension_ids(obj))
    refs.extend((x, 'business_rules') for x in rule_ids(obj))
    refs.extend((x, 'datasets') for x in dataset_ids(obj))
    for key, field in refs:
        if key not in catalog:
            raise ValueError(f"{obj['id']}: referência ausente em {field}: {key}")


def validate(catalog):
    for obj in catalog.values():
        if obj.get('status') not in ('draft', 'in_review', 'certified', 'deprecated'):
            raise ValueError(f"{obj['id']}: status inválido {obj.get('status')}")
        _validate_references(obj, catalog)
        _validate_certified(obj)

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


def build(catalog):
    target = ROOT / 'catalog'
    target.mkdir(exist_ok=True)
    indexes = {'metrics.json': index(catalog), 'all.json': all_index(catalog)}
    for object_type, filename in CATALOG_FILES.items():
        indexes[filename] = type_index(catalog, object_type)
    for filename, entries in indexes.items():
        (target / filename).write_text(json.dumps(entries, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')

    groups = {'catalogo': [], 'catalogo-tecnico': []}
    for obj in catalog.values():
        group = 'catalogo-tecnico' if obj['path'].startswith(('technical/', 'data_products/')) else 'catalogo'
        groups[group].append(obj)
    for name, entries in groups.items():
        lines = ['# ' + ('Catálogo de negócio' if name == 'catalogo' else 'Inventário técnico'),
                 '', 'Gerado por `python scripts/atlas.py build`. Todos os estados vêm dos contratos.', '',
                 '[Consulta curta](consulta.md) · [Negócio](catalogo.md) · [Técnico](catalogo-tecnico.md)', '',
                 '| ID | Nome | Tipo | Domínio | Status | Evidência |', '|---|---|---|---|---|---|']
        if name == 'catalogo-tecnico':
            lines.insert(4, 'Os objetos `tabela_*` são evidências técnicas legadas; novos datasets governados pertencem a `datasets/`.\n')
        for o in entries:
            lines.append(f"| [{o['id']}](<../{o['path']}>) | {o['title']} | {normalized_type(o)} | {o['domain']} | {o['status']} | {governance_state(o)} |")
        (ROOT / 'docs' / (name + '.md')).write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['search', 'search-all', 'show', 'build', 'validate'])
    parser.add_argument('query', nargs='?')
    parser.add_argument('--type', dest='object_type', choices=list(CATALOG_FILES))
    parser.add_argument('--limit', type=int, default=5)
    args = parser.parse_args()
    catalog = objects()
    validate(catalog)
    if args.command == 'build':
        build(catalog)
    elif args.command == 'validate':
        print(f'{len(catalog)} objetos; IDs, referências, certificação, dependências e ciclos verificados.')
    elif args.command == 'search':
        print(json.dumps(search(args.query or '', index(catalog), args.limit), ensure_ascii=False, indent=2))
    elif args.command == 'search-all':
        print(json.dumps(search_all(args.query or '', catalog, args.object_type, args.limit), ensure_ascii=False, indent=2))
    else:
        if args.query not in catalog:
            parser.error('ID não encontrado')
        obj = catalog[args.query]
        result = context(args.query, catalog) if obj.get('type') == 'metric' else get_object(args.query, catalog)
        print(json.dumps(result, ensure_ascii=False, indent=2, default=str))


if __name__ == '__main__':
    main()
