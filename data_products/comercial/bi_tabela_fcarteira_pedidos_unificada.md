---
schema_version: 1
id: "bi_tabela_fcarteira_pedidos_unificada"
title: "fCarteira_pedidos_unificada"
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
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/fCarteira_pedidos_unificada.tmdl"
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

# fCarteira_pedidos_unificada

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
      "comercial.fato_carteira_pedidos_planejamento"
    ],
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/fCarteira_pedidos_unificada.tmdl:203"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| data_carteira | dateTime | data_carteira | none | não declarado | Não declarada | 4 |
| ano_mes | string | ano_mes | none | não declarado | Não declarada | 15 |
| order_sale_order_code | int64 | order_sale_order_code | sum | não declarado | Não declarada | 23 |
| order_sale_order_date | dateTime | order_sale_order_date | none | não declarado | Não declarada | 32 |
| order_billing_billing_date | dateTime | order_billing_billing_date | none | não declarado | Não declarada | 43 |
| order_sale_program_date | dateTime | order_sale_program_date | none | não declarado | Não declarada | 54 |
| obt_sales_order_status | string | obt_sales_order_status | none | não declarado | Não declarada | 65 |
| obt_sales_order_type | string | obt_sales_order_type | none | não declarado | Não declarada | 73 |
| company | string | company | none | não declarado | Não declarada | 81 |
| order_sale_order_office_code | string | order_sale_order_office_code | none | não declarado | Não declarada | 89 |
| order_sale_material_code | string | order_sale_material_code | none | não declarado | Não declarada | 97 |
| order_sale_quantity | double | order_sale_quantity | sum | não declarado | Não declarada | 105 |
| order_sale_subtotal | double | order_sale_subtotal | sum | não declarado | Não declarada | 115 |
| order_billing_quantity | double | order_billing_quantity | sum | não declarado | Não declarada | 125 |
| order_billing_subtotal | double | order_billing_subtotal | sum | não declarado | Não declarada | 135 |
| obt_sales_department_status | string | obt_sales_department_status | none | não declarado | Não declarada | 145 |
| order_sale_storage_code | string | order_sale_storage_code | none | não declarado | Não declarada | 153 |
| order_sale_last_change_date_item | dateTime | order_sale_last_change_date_item | none | não declarado | Não declarada | 161 |
| status_carteira | string | status_carteira | none | não declarado | Não declarada | 172 |
| qt_ordem_carteira_inicial | double | qt_ordem_carteira_inicial | sum | não declarado | Não declarada | 180 |
| vr_item_carteira_inicial | double | vr_item_carteira_inicial | sum | não declarado | Não declarada | 190 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: fCarteira_pedidos_unificada

Tipo: m. Propriedades: `{"mode": "import", "queryGroup": "Fato"}`. Fonte: linha 203.

```powerquery
let
    Fonte = AmazonRedshift.Database("<endpoint na fonte original>","farmax_prod"),
    comercial = Fonte{[Name="comercial"]}[Data],
    fato_carteira_pedidos_planejamento = comercial{[Name="fato_carteira_pedidos_planejamento"]}[Data]
in
    fato_carteira_pedidos_planejamento
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 21 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 4. Consultar o [mapa do modelo](../../docs/powerbi/modelo.md).

Medidas com referência direta:

- [10 Carteira Inicial](<../../metrics/comercial/bi_10_carteira_inicial.yaml>)

## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/fCarteira_pedidos_unificada.tmdl>)
