---
schema_version: 1
id: "tabela_dempresa"
title: "dEmpresa"
type: "data_product"
domain: "comercial"
status: "draft"
version: "0.1.0"
owners:
  business: null
  technical: null
created_at: "2026-09-06"
updated_at: "2026-09-06"
sources:
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/dEmpresa.tmdl"
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

# dEmpresa

## Objetivo

Mapear a tabela, suas colunas e sua linhagem como evidência para o Atlas.

## Definição e escopo

Objeto técnico observado na exportação PBIP. Consumidores: modelo semântico e relatório Farmax v3 (1). Significado completo, granularidade e chaves naturais: pendentes de confirmação.

## Especificação

### Origem e linhagem

```json
[
  {
    "engine": "Power Platform Dataflow",
    "entities": [
      "dEmpresa"
    ],
    "upstream": null,
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/dEmpresa.tmdl:55"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| Company | string | Company | none | não declarado | Não declarada | 5 |
| Description | string | Description | none | não declarado | Não declarada | 15 |
| Cod_Origem | int64 | Cod_Origem | sum | não declarado | Não declarada | 25 |
| Grupo | string | Grupo | none | não declarado | Não declarada | 36 |
| Empresa | string | Empresa | none | não declarado | Não declarada | 44 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: dEmpresa-17376962-dc8c-41c7-8cde-55900ec5eb70

Tipo: m. Propriedades: `{"mode": "import", "queryGroup": "Dimensão"}`. Fonte: linha 55.

```powerquery
let
    Source = PowerPlatform.Dataflows([]),
    Workspaces = Source{[Id="Workspaces"]}[Data],
    #"4c88a2b6-9309-4368-9a28-168154f1d083" = Workspaces{[workspaceId="4c88a2b6-9309-4368-9a28-168154f1d083"]}[Data],
    #"e935f8e3-404f-4bbd-8fbb-8942c0e6f04e" = #"4c88a2b6-9309-4368-9a28-168154f1d083"{[dataflowId="e935f8e3-404f-4bbd-8fbb-8942c0e6f04e"]}[Data],
    dEmpresa_ = #"e935f8e3-404f-4bbd-8fbb-8942c0e6f04e"{[entity="dEmpresa",version=""]}[Data]
in
    dEmpresa_
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 5 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 7. Consultar o [mapa do modelo](../../docs/ingestoes/2026-09-06-modelo-corporativo/modelo.md).

Medidas com referência direta:

- [Pedidos & Faturamentos HTML](<../../technical/measures/corporativo/metrica_pedidos_e_faturamentos_html.yaml>)
- [Carteira e Estoque HTML v1](<../../technical/measures/corporativo/metrica_carteira_e_estoque_html_v1.yaml>)
- [Comercial HTML v1](<../../technical/measures/corporativo/metrica_comercial_html_v1.yaml>)
- [Farmax BI HTML old](<../../technical/measures/corporativo/metrica_farmax_bi_html_old.yaml>)
- [10 Carteira Inicial](<../../metrics/comercial/metrica_carteira_inicial.yaml>)
- [Farmax BI HTML v2](<../../technical/measures/corporativo/metrica_farmax_bi_html_v2.yaml>)
- [Pedidos & Faturamentos Menu HTML](<../../technical/measures/corporativo/metrica_pedidos_e_faturamentos_menu_html.yaml>)

## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/dEmpresa.tmdl>)
