---
schema_version: 1
id: "bi_tabela_fdevolucao_unificada"
title: "fDevolucao_unificada"
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
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/fDevolucao_unificada.tmdl"
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

# fDevolucao_unificada

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
      "comercial.fato_devolucao_unificada"
    ],
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/fDevolucao_unificada.tmdl:184"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| empresa | string | empresa | none | não declarado | Não declarada | 4 |
| companhia | string | companhia | none | não declarado | Não declarada | 12 |
| data_movimento | dateTime | data_movimento | none | não declarado | Não declarada | 20 |
| chave_executivo | string | chave_executivo | none | não declarado | Não declarada | 31 |
| cod_executivo | string | cod_executivo | none | não declarado | Não declarada | 39 |
| cod_coordenador | string | cod_coordenador | none | não declarado | Não declarada | 47 |
| chave_cliente | string | chave_cliente | none | não declarado | Não declarada | 55 |
| cod_cliente | string | cod_cliente | none | não declarado | Não declarada | 63 |
| estado | string | estado | none | não declarado | Não declarada | 71 |
| cidade | string | cidade | none | não declarado | Não declarada | 79 |
| nota_fiscal | string | nota_fiscal | none | não declarado | Não declarada | 87 |
| pedido | string | pedido | none | não declarado | Não declarada | 95 |
| sku | string | sku | none | não declarado | Não declarada | 103 |
| deposito_codigo | string | deposito_codigo | none | não declarado | Não declarada | 111 |
| regional_codigo | string | regional_codigo | none | não declarado | Não declarada | 119 |
| quantidade | double | quantidade | sum | não declarado | Não declarada | 127 |
| receita | double | receita | sum | não declarado | Não declarada | 137 |
| faturamento_cod_tipo | string | faturamento_cod_tipo | none | não declarado | Não declarada | 147 |
| devolucao_cod_tipo | string | devolucao_cod_tipo | none | não declarado | Não declarada | 155 |
| canal_n1 | string | canal_n1 | none | não declarado | Não declarada | 163 |
| receita_bruta | double | receita_bruta | sum | não declarado | Não declarada | 171 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: fDevolucao_unificada

Tipo: m. Propriedades: `{"mode": "import", "queryGroup": "Fato"}`. Fonte: linha 184.

```powerquery
let
    Source = AmazonRedshift.Database("<endpoint na fonte original>","farmax_prod"),
    comercial = Source{[Name="comercial"]}[Data],
    fato_devolucao_unificada1 = comercial{[Name="fato_devolucao_unificada"]}[Data]
in
    fato_devolucao_unificada1
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 21 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 6. Consultar o [mapa do modelo](../../docs/powerbi/modelo.md).

Medidas com referência direta:

- [00 Devolução](<../../metrics/comercial/bi_00_devolucao.yaml>)
- [01 Refaturamento](<../../metrics/comercial/bi_01_refaturamento.yaml>)
- [04 RSL Ano Atual](<../../metrics/comercial/bi_04_rsl_ano_atual.yaml>)

## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/fDevolucao_unificada.tmdl>)
