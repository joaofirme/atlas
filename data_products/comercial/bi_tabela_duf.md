---
schema_version: 1
id: "bi_tabela_duf"
title: "dUF"
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
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/dUF.tmdl"
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

# dUF

## Objetivo

Mapear a tabela semântica e sua linhagem no BI corporativo.

## Definição e escopo

Objeto técnico observado na exportação PBIP. Consumidores: modelo semântico e relatório Farmax v3 (1). Significado completo, granularidade e chaves naturais: pendentes de confirmação.

## Especificação

### Origem e linhagem

```json
[
  {
    "engine": "Power Platform Dataflow",
    "entities": [
      "dUF"
    ],
    "upstream": null,
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/dUF.tmdl:191"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| uf | string | uf | none | não declarado | Não declarada | 4 |
| estado | string | estado | none | não declarado | Não declarada | 12 |
| area | int64 | area | sum | não declarado | Não declarada | 20 |
| den_demografica | int64 | den_demografica | sum | não declarado | Não declarada | 29 |
| Pop_10 | int64 | Pop_10 | sum | não declarado | Não declarada | 38 |
| Pop_21 | int64 | Pop_21 | sum | não declarado | Não declarada | 47 |
| pop_var | int64 | pop_var | sum | não declarado | Não declarada | 56 |
| var | string | var | none | não declarado | Não declarada | 65 |
| pib_10 | int64 | pib_10 | sum | não declarado | Não declarada | 73 |
| pip_21 | int64 | pip_21 | sum | não declarado | Não declarada | 82 |
| pib_var | string | pib_var | none | não declarado | Não declarada | 91 |
| idh_10 | string | idh_10 | none | não declarado | Não declarada | 99 |
| idh_21 | string | idh_21 | none | não declarado | Não declarada | 107 |
| idh_var | string | idh_var | none | não declarado | Não declarada | 115 |
| rend_domiciliar_10 | int64 | rend_domiciliar_10 | sum | não declarado | Não declarada | 123 |
| rend_domiciliar_21 | int64 | rend_domiciliar_21 | sum | não declarado | Não declarada | 132 |
| rend_var | string | rend_var | none | não declarado | Não declarada | 141 |
| taxa_urbana_10 | string | taxa_urbana_10 | none | não declarado | Não declarada | 149 |
| taxa_rural_10 | string | taxa_rural_10 | none | não declarado | Não declarada | 157 |
| taxa_urbana_21 | string | taxa_urbana_21 | none | não declarado | Não declarada | 165 |
| taxa_rural_21 | string | taxa_rural_21 | none | não declarado | Não declarada | 173 |
| regiao | string | regiao | none | não declarado | Não declarada | 181 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: dUF

Tipo: m. Propriedades: `{"mode": "import"}`. Fonte: linha 191.

```powerquery
let
    Fonte = PowerPlatform.Dataflows(null),
    Workspaces = Fonte{[Id="Workspaces"]}[Data],
    #"4c88a2b6-9309-4368-9a28-168154f1d083" = Workspaces{[workspaceId="4c88a2b6-9309-4368-9a28-168154f1d083"]}[Data],
    #"e935f8e3-404f-4bbd-8fbb-8942c0e6f04e" = #"4c88a2b6-9309-4368-9a28-168154f1d083"{[dataflowId="e935f8e3-404f-4bbd-8fbb-8942c0e6f04e"]}[Data],
    dUF_ = #"e935f8e3-404f-4bbd-8fbb-8942c0e6f04e"{[entity="dUF",version=""]}[Data]
in
    dUF_
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 22 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 0. Consultar o [mapa do modelo](../../docs/powerbi/modelo.md).

Medidas com referência direta:



## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/dUF.tmdl>)
