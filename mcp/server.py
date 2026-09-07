"""Servidor MCP read-only da Alexandria."""
import importlib.util
from pathlib import Path
from typing import Literal

from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('atlas_catalog', ROOT / 'scripts' / 'atlas.py')
atlas = importlib.util.module_from_spec(spec)
spec.loader.exec_module(atlas)

mcp = FastMCP('Alexandria', instructions=(
    'Consulte a fonte semântica governada da Farmax. Objetos observed/draft são '
    'evidência, não verdade oficial. Este servidor nunca consulta ou altera dados.'))


def _catalog():
    catalog = atlas.objects()
    atlas.validate(catalog)
    return catalog


@mcp.tool()
def search_alexandria(query: str, object_type: Literal['all', 'metric', 'dimension',
                      'dataset', 'business_rule', 'concept', 'analysis_skill'] = 'all',
                      certified_only: bool = False, limit: int = 10) -> list[dict]:
    """Busca contratos por linguagem de negócio, retornando status e autoridade."""
    types = None if object_type == 'all' else [object_type]
    return atlas.search_all(query, _catalog(), types, min(max(limit, 1), 25), certified_only)


def _get(identifier: str, expected_type: str) -> dict:
    catalog = _catalog()
    obj = atlas.public_object(identifier, catalog)
    if obj['type'] != expected_type:
        raise ValueError(f'{identifier} é {obj["type"]}, não {expected_type}')
    return atlas.context(identifier, catalog) if expected_type == 'metric' else obj


@mcp.tool()
def get_metric(identifier: str) -> dict:
    """Obtém uma métrica, dependências, dimensões, datasets e regras."""
    return _get(identifier, 'metric')


@mcp.tool()
def get_dimension(identifier: str) -> dict:
    """Obtém o contrato read-only de uma dimensão."""
    return _get(identifier, 'dimension')


@mcp.tool()
def get_dataset(identifier: str) -> dict:
    """Obtém um dataset de negócio e sua rastreabilidade de implementação."""
    return _get(identifier, 'dataset')


@mcp.tool()
def get_business_rule(identifier: str) -> dict:
    """Obtém uma regra de negócio e seu estado de aprovação."""
    return _get(identifier, 'business_rule')


@mcp.tool()
def get_concept(identifier: str) -> dict:
    """Obtém um conceito do vocabulário de negócio."""
    return _get(identifier, 'concept')


@mcp.tool()
def get_skill(identifier: str) -> dict:
    """Obtém um procedimento analítico sem executá-lo."""
    return _get(identifier, 'analysis_skill')


if __name__ == '__main__':
    mcp.run()
