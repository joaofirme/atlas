"""Busca local e índices derivados. Não executa consultas aos dados da Farmax."""
import argparse
import json
import re
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = ('metrics', 'technical', 'dimensions', 'ontology', 'business_rules', 'data_products', 'skills')


def objects():
    result = {}
    for folder in FOLDERS:
        for path in sorted((ROOT / folder).rglob('*')):
            if path.suffix not in ('.yaml', '.md'):
                continue
            text = path.read_text(encoding='utf-8')
            if path.suffix == '.md':
                if not text.startswith('---\n'):
                    continue
                text = text.split('---', 2)[1]
            obj = yaml.safe_load(text)
            obj = obj.get('metadata', obj)
            if obj['id'] in result:
                raise ValueError('ID duplicado: ' + obj['id'])
            result[obj['id']] = {**obj, 'path': path.relative_to(ROOT).as_posix()}
    return result


def normalize(value):
    value = unicodedata.normalize('NFKD', value.lower())
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


def index(catalog):
    return [dict(id=o['id'], title=o['title'], synonyms=o.get('synonyms') or [],
                 questions=o.get('business_questions') or [], status=o['status'], path=o['path'])
            for o in catalog.values() if o['path'].startswith('metrics/')]


def search(query, entries, limit=5):
    words = set(normalize(query).split()) - {'a', 'o', 'as', 'os', 'de', 'da', 'do', 'em', 'quanto', 'qual', 'que', 'estao'}
    ranked = []
    for entry in entries:
        labels = [entry['id'], entry['title'], *entry['synonyms'], *entry['questions']]
        score = max((len(words & set(normalize(s).split())) / max(len(words), 1)
                     + (2 if normalize(query) == normalize(s) else 0) for s in labels), default=0)
        if score:
            ranked.append((score, entry))
    return [{**entry, 'score': round(score, 3)} for score, entry in
            sorted(ranked, key=lambda pair: (-pair[0], pair[1]['id']))[:limit]]


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
    pages = json.loads((ROOT / 'docs/ingestoes/2026-09-06-modelo-corporativo/uso_no_relatorio.json').read_text(encoding='utf-8'))
    names = {s for key in [identifier, *impacts] for s in catalog[key].get('synonyms', [])}
    uses = []
    for page in pages:
        for visual in page['visuals']:
            refs = sorted({r['property'] for r in visual['refs'] if r['kind'] == 'Measure' and r['property'] in names})
            if refs:
                uses.append(dict(page=page['title'], visibility=page['visibility'], measures=refs,
                                 source=visual['source'], note='Referência direta ou dependência transitiva; verificar filtros e ramos condicionais no visual.'))
    ref = lambda key: {'id': key, 'path': catalog[key]['path']}
    guidance = [ref(key) for key, item in catalog.items()
                if item['type'] in ('analysis_skill', 'business_rule', 'concept')
                and identifier in (ROOT / item['path']).read_text(encoding='utf-8')]
    return dict(metric=obj, dependencies=[ref(k) for k in sorted(chain - {identifier})],
                impacts=[ref(k) for k in sorted(impacts)],
                candidate_dimensions=[ref(o['id']) for o in dims],
                observed_relationships=[ref(o['id']) for o in relations], report_usage=uses,
                analysis_guidance=guidance,
                limitations='Dimensões e joins observados não são aprovados. Uso transitivo não comprova exibição. Sem dados atuais ou execução DAX. Abrir apenas as referências necessárias.')


def validate(catalog):
    for obj in catalog.values():
        for key in dependencies(obj):
            if key not in catalog:
                raise ValueError(f"{obj['id']}: dependência ausente {key}")
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
    (target / 'metrics.json').write_text(json.dumps(index(catalog), ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
    groups = {'catalogo': [], 'catalogo-tecnico': []}
    for obj in catalog.values():
        group = 'catalogo-tecnico' if obj['path'].startswith(('technical/', 'data_products/')) else 'catalogo'
        groups[group].append(obj)
    for name, entries in groups.items():
        lines = ['# ' + ('Catálogo de negócio' if name == 'catalogo' else 'Inventário técnico'),
                 '', 'Gerado por `python scripts/atlas.py build`. Todos os estados vêm dos contratos.', '',
                 '[Consulta curta](consulta.md) · [Negócio](catalogo.md) · [Técnico](catalogo-tecnico.md)', '',
                 '| ID | Nome | Tipo | Domínio | Status |', '|---|---|---|---|---|']
        if name == 'catalogo-tecnico':
            lines.insert(4, 'Os objetos `tabela_*` são documentação de tabelas da carga inicial; o tipo legado `data_product` não comprova produto governado.\n')
        for o in entries:
            lines.append(f"| [{o['id']}](<../{o['path']}>) | {o['title']} | {o['type']} | {o['domain']} | {o['status']} |")
        (ROOT / 'docs' / (name + '.md')).write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['search', 'show', 'build', 'validate'])
    parser.add_argument('query', nargs='?')
    args = parser.parse_args()
    catalog = objects()
    validate(catalog)
    if args.command == 'build':
        build(catalog)
    elif args.command == 'validate':
        print(f'{len(catalog)} objetos; IDs, dependências e ciclos verificados.')
    elif args.command == 'search':
        print(json.dumps(search(args.query or '', index(catalog)), ensure_ascii=False, indent=2))
    else:
        if args.query not in catalog:
            parser.error('ID não encontrado')
        print(json.dumps(context(args.query, catalog), ensure_ascii=False, indent=2, default=str))


if __name__ == '__main__':
    main()
