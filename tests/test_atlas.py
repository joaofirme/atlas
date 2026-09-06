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
