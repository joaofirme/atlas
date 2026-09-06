---
schema_version: 1
id: "bi_tabela_fvendas_unificada"
title: "fVendas_unificada"
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
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/fVendas_unificada.tmdl"
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

# fVendas_unificada

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
      "comercial.fato_vendas_faturamento_unificada"
    ],
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/fVendas_unificada.tmdl:480"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| empresa | string | empresa | none | não declarado | Não declarada | 4 |
| companhia | string | companhia | none | não declarado | Não declarada | 12 |
| data_movimento | dateTime | data_movimento | none | não declarado | Não declarada | 20 |
| data_pedido | dateTime | data_pedido | none | não declarado | Não declarada | 31 |
| cod_executivo | int64 | cod_executivo | sum | não declarado | Não declarada | 42 |
| cod_coordenador | string | cod_coordenador | none | não declarado | Não declarada | 51 |
| chave_cliente | string | chave_cliente | none | não declarado | Não declarada | 59 |
| cod_cliente | int64 | cod_cliente | sum | não declarado | Não declarada | 67 |
| cpf_cnpj_base | string | cpf_cnpj_base | none | não declarado | Não declarada | 76 |
| estado | string | estado | none | não declarado | Não declarada | 84 |
| cidade | string | cidade | none | não declarado | Não declarada | 92 |
| nota_fiscal | int64 | nota_fiscal | sum | não declarado | Não declarada | 100 |
| pedido | int64 | pedido | sum | não declarado | Não declarada | 109 |
| sku | string | sku | none | não declarado | Não declarada | 118 |
| categoria | string | categoria | none | não declarado | Não declarada | 126 |
| canal_n1 | string | canal_n1 | none | não declarado | Não declarada | 134 |
| data_lancamento | dateTime | data_lancamento | none | não declarado | Não declarada | 142 |
| pedido_tipo | string | pedido_tipo | none | não declarado | Não declarada | 153 |
| venda_cod_tipo | string | venda_cod_tipo | none | não declarado | Não declarada | 161 |
| pedido_status | string | pedido_status | none | não declarado | Não declarada | 169 |
| regional_cod | string | regional_cod | none | não declarado | Não declarada | 177 |
| ledger_net_subtotal | double | ledger_net_subtotal | sum | não declarado | Não declarada | 185 |
| quantidade | int64 | quantidade | sum | não declarado | Não declarada | 195 |
| quantidade_venda | int64 | quantidade_venda | sum | não declarado | Não declarada | 204 |
| receita | double | receita | sum | não declarado | Não declarada | 213 |
| receita_bruta | double | receita_bruta | sum | não declarado | Não declarada | 223 |
| customer_regiao | string | customer_regiao | none | não declarado | Não declarada | 233 |
| material_group_code | string | material_group_code | none | não declarado | Não declarada | 241 |
| material_medication | string | material_medication | none | não declarado | Não declarada | 249 |
| order_sale_quantity | int64 | order_sale_quantity | sum | não declarado | Não declarada | 257 |
| order_sale_delivery_quantity | int64 | order_sale_delivery_quantity | sum | não declarado | Não declarada | 266 |
| order_sale_cut_value | int64 | order_sale_cut_value | sum | não declarado | Não declarada | 275 |
| order_sale_subtotal | double | order_sale_subtotal | sum | não declarado | Não declarada | 284 |
| sale_rejection_reason_code | string | sale_rejection_reason_code | none | não declarado | Não declarada | 294 |
| sale_billing_block_code | string | sale_billing_block_code | none | não declarado | Não declarada | 302 |
| sale_delivery_code | int64 | sale_delivery_code | sum | não declarado | Não declarada | 310 |
| sale_delivery_block_code | string | sale_delivery_block_code | none | não declarado | Não declarada | 319 |
| sale_delivery_item_block_code | string | sale_delivery_item_block_code | none | não declarado | Não declarada | 327 |
| sale_storage_code | int64 | sale_storage_code | sum | não declarado | Não declarada | 335 |
| sale_shipping_code | int64 | sale_shipping_code | sum | não declarado | Não declarada | 344 |
| sale_shipping_type | string | sale_shipping_type | none | não declarado | Não declarada | 353 |
| sale_program_date | dateTime | sale_program_date | none | não declarado | Não declarada | 361 |
| sale_cancellation_date | dateTime | sale_cancellation_date | none | não declarado | Não declarada | 372 |
| customer_license_zc0001_to | dateTime | customer_license_zc0001_to | none | não declarado | Não declarada | 383 |
| customer_license_zc0002_to | dateTime | customer_license_zc0002_to | none | não declarado | Não declarada | 394 |
| customer_customer_type_code | int64 | customer_customer_type_code | sum | não declarado | Não declarada | 405 |
| customer_flag_customer_analytics | int64 | customer_flag_customer_analytics | sum | não declarado | Não declarada | 414 |
| obt_sales_department_status | string | obt_sales_department_status | none | não declarado | Não declarada | 423 |
| sale_customer | string | sale_customer | none | não declarado | Não declarada | 431 |
| material_brand_code | int64 | material_brand_code | sum | não declarado | Não declarada | 439 |
| chave_executivo | string | chave_executivo | none | não declarado | Não declarada | 448 |
| data_entrega | dateTime | data_entrega | none | não declarado | Não declarada | 456 |
| order_sale_total | double | order_sale_total | sum | não declarado | Não declarada | 467 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: fVendas_unificada

Tipo: m. Propriedades: `{"mode": "import", "queryGroup": "Fato"}`. Fonte: linha 480.

```powerquery
let
    Source = AmazonRedshift.Database("<endpoint na fonte original>","farmax_prod"),
    comercial = Source{[Name="comercial"]}[Data],
    fato_vendas_faturamento_unificada = comercial{[Name="fato_vendas_faturamento_unificada"]}[Data],
    #"Filtered Rows" = Table.SelectRows(fato_vendas_faturamento_unificada, each [data_pedido] > #date(2024, 1, 1)),
    #"Changed Type" = Table.TransformColumnTypes(#"Filtered Rows",{{"empresa", type text}, {"companhia", type text}, {"data_movimento", type date}, {"data_pedido", type date}, {"cod_executivo", Int64.Type}, {"cod_coordenador", type text}, {"chave_cliente", type text}, {"cod_cliente", Int64.Type}, {"cpf_cnpj_base", type text}, {"estado", type text}, {"cidade", type text}, {"nota_fiscal", Int64.Type}, {"pedido", Int64.Type}, {"sku", type text}, {"categoria", type text}, {"canal_n1", type text}, {"data_lancamento", type date}, {"pedido_tipo", type text}, {"venda_cod_tipo", type text}, {"pedido_status", type text}, {"regional_cod", type text}, {"ledger_net_subtotal", type number}, {"quantidade", Int64.Type}, {"quantidade_venda", Int64.Type}, {"receita", type number}, {"receita_bruta", type number}, {"customer_regiao", type text}, {"material_group_code", type text}, {"material_medication", type text}, {"order_sale_quantity", Int64.Type}, {"order_sale_delivery_quantity", Int64.Type}, {"order_sale_cut_value", Int64.Type}, {"order_sale_subtotal", type number}, {"sale_rejection_reason_code", type text}, {"sale_billing_block_code", type text}, {"sale_delivery_code", Int64.Type}, {"sale_delivery_block_code", type text}, {"sale_delivery_item_block_code", type text}, {"sale_storage_code", Int64.Type}, {"sale_shipping_code", Int64.Type}, {"sale_shipping_type", type text}, {"sale_program_date", type date}, {"sale_cancellation_date", type date}, {"customer_license_zc0001_to", type date}, {"customer_license_zc0002_to", type date}, {"customer_customer_type_code", Int64.Type}, {"customer_flag_customer_analytics", Int64.Type}, {"obt_sales_department_status", type text}, {"sale_customer", type text}, {"material_brand_code", Int64.Type}})
in
    #"Changed Type"
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 53 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 8. Consultar o [mapa do modelo](../../docs/powerbi/modelo.md).

Medidas com referência direta:

- [03 Total a Faturar](<../../metrics/comercial/bi_03_total_a_faturar.yaml>)
- [04 RSL Ano Atual](<../../metrics/comercial/bi_04_rsl_ano_atual.yaml>)
- [06 Aguarda Produção](<../../metrics/comercial/bi_06_aguarda_producao.yaml>)
- [01 Unidades Faturadas](<../../metrics/comercial/bi_01_unidades_faturadas.yaml>)
- [01 Em Análise](<../../metrics/financeiro/bi_01_em_analise.yaml>)
- [04 Aberto](<../../metrics/comercial/bi_04_aberto.yaml>)
- [05 Programado](<../../metrics/comercial/bi_05_programado.yaml>)
- [00 Faturamento](<../../metrics/comercial/bi_00_faturamento.yaml>)
- [01 Unidades Vendidas](<../../metrics/comercial/bi_01_unidades_vendidas.yaml>)
- [00 Valor de Vendas](<../../metrics/comercial/bi_00_valor_de_vendas.yaml>)
- [06 RL](<../../metrics/comercial/bi_06_rl.yaml>)
- [07 Aguarda Produção Soro](<../../metrics/comercial/bi_07_aguarda_producao_soro.yaml>)
- [08 Aguarda Produção sem Soro](<../../metrics/comercial/bi_08_aguarda_producao_sem_soro.yaml>)
- [05 Programado M+](<../../metrics/comercial/bi_05_programado_m_mais.yaml>)
- [04 RSL YoY Aberto %](<../../metrics/comercial/bi_04_rsl_yoy_aberto_percentual.yaml>)
- [04 RSL MoM Aberto %](<../../metrics/comercial/bi_04_rsl_mom_aberto_percentual.yaml>)
- [04 % Vendas MoM](<../../metrics/comercial/bi_04_percentual_vendas_mom.yaml>)
- [04 % Vendas YoY](<../../metrics/comercial/bi_04_percentual_vendas_yoy.yaml>)
- [04 % Unidades MoM](<../../metrics/comercial/bi_04_percentual_unidades_mom.yaml>)
- [04 % Unidades YoY](<../../metrics/comercial/bi_04_percentual_unidades_yoy.yaml>)
- [08 Faturamento Bruto](<../../metrics/comercial/bi_08_faturamento_bruto.yaml>)
- [Carteira e Estoque HTML v1](<../../metrics/corporativo/bi_carteira_e_estoque_html_v1.yaml>)
- [Comercial HTML v1](<../../metrics/corporativo/bi_comercial_html_v1.yaml>)
- [06 Valor Entregue](<../../metrics/comercial/bi_06_valor_entregue.yaml>)
- [02 Cancelado](<../../metrics/comercial/bi_02_cancelado.yaml>)
- [06 Ret.-Limit.créd.exc.](<../../metrics/financeiro/bi_06_ret_limit_cred_exc.yaml>)
- [00 Financeiro](<../../metrics/financeiro/bi_00_financeiro.yaml>)
- [00 Logística](<../../metrics/logistica/bi_00_logistica.yaml>)
- [07 Valor Em Transito](<../../metrics/logistica/bi_07_valor_em_transito.yaml>)
- [00 Customer Service](<../../metrics/comercial/bi_00_customer_service.yaml>)

## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/fVendas_unificada.tmdl>)
