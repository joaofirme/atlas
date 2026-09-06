---
schema_version: 1
id: "tabela_fmeta_unificada"
title: "fMeta_unificada"
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
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/fMeta_unificada.tmdl"
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

# fMeta_unificada

## Objetivo

Mapear a tabela, suas colunas e sua linhagem como evidência para o Atlas.

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
      "comercial.fato_metas_executivos_unificada"
    ],
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/fMeta_unificada.tmdl:128"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| chave_origem | string | chave_origem | none | não declarado | Não declarada | 4 |
| empresa | string | empresa | none | não declarado | Não declarada | 12 |
| companhia | string | companhia | none | não declarado | Não declarada | 20 |
| cod_executivo | string | cod_executivo | none | não declarado | Não declarada | 28 |
| chave_coordenador | string | chave_coordenador | none | não declarado | Não declarada | 36 |
| chave_regional | string | chave_regional | none | não declarado | Não declarada | 44 |
| chave_segmento | string | chave_segmento | none | não declarado | Não declarada | 52 |
| chave_marca | string | chave_marca | none | não declarado | Não declarada | 60 |
| meta_receita | double | meta_receita | sum | não declarado | Não declarada | 68 |
| meta_positivacao | double | meta_positivacao | sum | não declarado | Não declarada | 78 |
| meta_ticket_medio | double | meta_ticket_medio | sum | não declarado | Não declarada | 88 |
| meta_data_alvo | dateTime | meta_data_alvo | none | não declarado | Não declarada | 98 |
| canal_vendas | string | canal_vendas | none | não declarado | Não declarada | 109 |
| chave_executivo | string | chave_executivo | none | não declarado | Não declarada | 117 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: fMeta_unificada

Tipo: m. Propriedades: `{"mode": "import", "queryGroup": "Fato"}`. Fonte: linha 128.

```powerquery
let
    Source = AmazonRedshift.Database("<endpoint na fonte original>","farmax_prod"),
    comercial = Source{[Name="comercial"]}[Data],
    fato_metas_executivos_unificada = comercial{[Name="fato_metas_executivos_unificada"]}[Data]
in
    fato_metas_executivos_unificada
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 14 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 5. Consultar o [mapa do modelo](../../docs/ingestoes/2026-09-06-modelo-corporativo/modelo.md).

Medidas com referência direta:

- [Meta Média](<../../metrics/comercial/metrica_meta_media.yaml>)
- [Meta RSL](<../../metrics/comercial/metrica_meta_rsl.yaml>)

## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/fMeta_unificada.tmdl>)
