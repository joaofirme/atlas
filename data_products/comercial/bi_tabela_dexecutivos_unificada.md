---
schema_version: 1
id: "bi_tabela_dexecutivos_unificada"
title: "dExecutivos_unificada"
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
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/dExecutivos_unificada.tmdl"
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

# dExecutivos_unificada

## Objetivo

Mapear a tabela semântica e sua linhagem no BI corporativo.

## Definição e escopo

Objeto técnico observado na exportação PBIP. Consumidores: modelo semântico e relatório Farmax v3 (1). Significado completo, granularidade e chaves naturais: pendentes de confirmação.

## Especificação

### Origem e linhagem

```json
[
  {
    "engine": "Amazon Redshift",
    "database": "farmax_prod",
    "objects": [
      "comercial.dimensao_executivos_unificada"
    ],
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/dExecutivos_unificada.tmdl:104"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| empresa | string | empresa | none | não declarado | Não declarada | 4 |
| executivo_chave | string | executivo_chave | none | não declarado | Não declarada | 12 |
| executivo_cod | int64 | executivo_cod | sum | não declarado | Não declarada | 20 |
| executivo_nome | string | executivo_nome | none | não declarado | Não declarada | 29 |
| executivo_email | string | executivo_email | none | não declarado | Não declarada | 37 |
| coordenador_cod | string | coordenador_cod | none | não declarado | Não declarada | 45 |
| coordenador_nome | string | coordenador_nome | none | não declarado | Não declarada | 53 |
| coordenador_email | string | coordenador_email | none | não declarado | Não declarada | 61 |
| regional_cod | string | regional_cod | none | não declarado | Não declarada | 69 |
| gerente_regional_nome | string | gerente_regional_nome | none | não declarado | Não declarada | 77 |
| gerente_email | string | gerente_email | none | não declarado | Não declarada | 85 |
| nome_unificado | string | nome_unificado | none | não declarado | Não declarada | 93 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: dExecutivos_unificada

Tipo: m. Propriedades: `{"mode": "import", "queryGroup": "Dimensão"}`. Fonte: linha 104.

```powerquery
let
    Source = AmazonRedshift.Database("<endpoint na fonte original>","farmax_prod"),
    comercial = Source{[Name="comercial"]}[Data],
    dimensao_executivos_unificada1 = comercial{[Name="dimensao_executivos_unificada"]}[Data],
    #"Changed Type" = Table.TransformColumnTypes(dimensao_executivos_unificada1,{{"empresa", type text}, {"executivo_chave", type text}, {"executivo_cod", Int64.Type}, {"executivo_nome", type text}, {"executivo_email", type text}, {"coordenador_cod", type text}, {"coordenador_nome", type text}, {"coordenador_email", type text}, {"regional_cod", type text}, {"gerente_regional_nome", type text}, {"gerente_email", type text}, {"nome_unificado", type text}}),
    #"Reordered Columns" = Table.ReorderColumns(#"Changed Type",{"empresa", "executivo_chave", "executivo_cod", "executivo_nome", "executivo_email", "coordenador_cod", "coordenador_nome", "coordenador_email", "regional_cod", "gerente_regional_nome", "gerente_email", "nome_unificado"})
in
    #"Reordered Columns"
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 12 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 4. Consultar o [mapa do modelo](../../docs/powerbi/modelo.md).

Medidas com referência direta:



## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/dExecutivos_unificada.tmdl>)
