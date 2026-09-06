---
schema_version: 1
id: "tabela_base_receita"
title: "Base Receita"
type: "data_product"
domain: "corporativo"
status: "draft"
version: "0.1.0"
owners:
  business: null
  technical: null
created_at: "2026-09-06"
updated_at: "2026-09-06"
sources:
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/Base Receita.tmdl"
    locator: "arquivo completo"
    accessed_at: "2026-09-06"
validation:
  reviewed_by: null
  reviewed_at: null
  evidence:
    - "Extração estática dos arquivos PBIP/TMDL; nenhuma execução de DAX/M ou consulta aos dados."
pending:
  - "Confirmar responsável de negócio e responsável técnico."
  - "Revisar semântica com a área e validar resultados no modelo em execução."
---

# Base Receita

## Objetivo

Mapear a tabela, suas colunas e sua linhagem como evidência para o Atlas.

## Definição e escopo

Objeto técnico observado na exportação PBIP. Consumidores: modelo semântico e relatório Farmax v3 (1). Significado completo, granularidade e chaves naturais: pendentes de confirmação.

## Especificação

### Origem e linhagem

```json
[
  {
    "engine": "DAX calculado",
    "upstream": null,
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/Base Receita.tmdl:23"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| Base Receita | Pendente | [Base Receita] | none | não declarado | Não declarada | 4 |
| Ordem | Pendente | [Ordem] | sum | não declarado | Não declarada | 12 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: Base Receita

Tipo: calculated. Propriedades: `{"mode": "import"}`. Fonte: linha 23.

```dax
DATATABLE(
    "Base Receita", STRING,
    "Ordem", INTEGER,
    {
        {"Receita Semi Liquida", 1},
        {"Receita Bruta", 2}
    }
)
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 2 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 0. Consultar o [mapa do modelo](../../docs/ingestoes/2026-09-06-modelo-corporativo/modelo.md).

Medidas com referência direta:

- [Pedidos & Faturamentos HTML](<../../technical/measures/corporativo/metrica_pedidos_e_faturamentos_html.yaml>)
- [Carteira e Estoque HTML v1](<../../technical/measures/corporativo/metrica_carteira_e_estoque_html_v1.yaml>)
- [Comercial HTML v1](<../../technical/measures/corporativo/metrica_comercial_html_v1.yaml>)
- [06 Valor Entregue](<../../metrics/comercial/metrica_valor_entregue.yaml>)
- [Farmax BI HTML old](<../../technical/measures/corporativo/metrica_farmax_bi_html_old.yaml>)
- [Faturamento Selecionado](<../../technical/measures/comercial/metrica_faturamento_selecionado.yaml>)
- [% Meta Exibição](<../../technical/measures/comercial/metrica_percentual_meta_exibicao.yaml>)
- [Devolução Selecionada](<../../technical/measures/comercial/metrica_devolucao_selecionada.yaml>)
- [Legenda Base Receita](<../../technical/measures/comercial/metrica_legenda_base_receita.yaml>)
- [Meta RSL Exibição](<../../technical/measures/comercial/metrica_meta_rsl_exibicao.yaml>)
- [Receita Selecionada](<../../technical/measures/comercial/metrica_receita_selecionada.yaml>)
- [Matriz RSL > Meta](<../../technical/measures/comercial/metrica_matriz_rsl_meta.yaml>)
- [Farmax BI HTML v2](<../../technical/measures/corporativo/metrica_farmax_bi_html_v2.yaml>)
- [Pedidos & Faturamentos Menu HTML](<../../technical/measures/corporativo/metrica_pedidos_e_faturamentos_menu_html.yaml>)

## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/Base Receita.tmdl>)
