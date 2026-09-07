import importlib.util
import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('atlas', ROOT / 'scripts/atlas.py')
atlas = importlib.util.module_from_spec(spec)
spec.loader.exec_module(atlas)


class AtlasTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = atlas.objects()

    def test_integrity(self):
        atlas.validate(self.catalog)

    def test_query_and_ambiguity(self):
        hits = atlas.search('quanto de receita a faturar estão abertas', atlas.index(self.catalog))
        self.assertEqual(hits[0]['id'], 'metrica_aberto')
        self.assertIn('metrica_total_a_faturar', [h['id'] for h in hits])
        self.assertEqual(atlas.search('05 Programado', atlas.index(self.catalog))[0]['id'], 'metrica_programado')
        self.assertEqual(atlas.search('xyzzy qwerty', atlas.index(self.catalog)), [])

    def test_business_index_excludes_presentation(self):
        entries = atlas.index(self.catalog)
        self.assertEqual(len(entries), sum(o.get('kind') == 'indicador' for o in self.catalog.values()))
        self.assertTrue(all(self.catalog[e['id']]['kind'] == 'indicador' for e in entries))
        saved = json.loads((ROOT / 'catalog/metrics.json').read_text(encoding='utf-8'))
        self.assertEqual(saved, entries)

    def test_all_business_indexes_are_generated(self):
        for object_type, filename in atlas.INDEX_TYPES.items():
            saved = json.loads((ROOT / 'catalog' / filename).read_text(encoding='utf-8'))
            self.assertEqual(saved, atlas.index(self.catalog, object_type))

    def test_cross_type_search_and_authority(self):
        hits = atlas.search_all('qual dataset usar para vendas', self.catalog)
        self.assertEqual(hits[0]['id'], 'dataset_vendas')
        self.assertEqual(atlas.public_object('dataset_vendas', self.catalog)['authority'],
                         'observed_not_official')
        self.assertEqual(atlas.search_all('vendas', self.catalog, certified_only=True), [])

    def test_certified_contract_requires_governance(self):
        incomplete = {
            'id': 'metrica_teste', 'title': 'Teste', 'type': 'metric',
            'domain': 'comercial', 'status': 'certified', 'evidence_status': 'observed',
            'version': '1.0.0', 'owners': {'business': None, 'technical': None},
            'definition': 'Definição', 'sources': [], 'validation': {},
            'formula': {'dependencies': []}}
        with self.assertRaisesRegex(ValueError, 'certified incompleto'):
            atlas.validate({'metrica_teste': incomplete})

    def test_metric_dataset_dimension_rule_links(self):
        item = atlas.context('metrica_aberto', self.catalog)
        self.assertIn('dataset_vendas', [x['id'] for x in item['datasets']])
        self.assertIn('dimensao_cliente', [x['id'] for x in item['linked_dimensions']])
        self.assertIn('regra_carteira_data_referencia',
                      [x['id'] for x in item['business_rules']])

    def test_context_has_transitive_evidence(self):
        context = atlas.context('metrica_aberto', self.catalog)
        self.assertIn('metrica_total_a_faturar', [x['id'] for x in context['dependencies']])
        self.assertIn('metrica_rsl_mais_aberto', [x['id'] for x in context['impacts']])
        self.assertIn('dimensao_cliente', [x['id'] for x in context['candidate_dimensions']])
        self.assertTrue(context['report_usage'])
        for usage in context['report_usage']:
            self.assertTrue((ROOT / usage['source']).exists())

    def test_cycle_and_missing_dependency_rejected(self):
        with self.assertRaises(ValueError):
            atlas.validate({'a': {'id': 'a', 'formula': {'dependencies': ['missing']}}})
        with self.assertRaises(ValueError):
            atlas.validate({'a': {'id': 'a', 'formula': {'dependencies': ['a']}}})

    def test_markdown_links(self):
        for path in ROOT.rglob('*.md'):
            if '.git' in path.parts:
                continue
            for match in re.finditer(r'\]\((<[^>]+>|[^)]+)\)', path.read_text(encoding='utf-8')):
                target = match.group(1).strip('<>').split('#')[0]
                if not target or '://' in target or target.startswith('mailto:'):
                    continue
                self.assertTrue((path.parent / target).exists() or (path.parent / unquote(target)).exists(), f'{path.relative_to(ROOT)} -> {target}')


if __name__ == '__main__':
    unittest.main()
