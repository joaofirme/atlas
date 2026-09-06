---
schema_version: 1
id: "tabela_tlogistica_e_cs"
title: "tLogistica e CS"
type: "data_product"
domain: "logistica"
status: "draft"
version: "0.1.0"
owners:
  business: null
  technical: null
created_at: "2026-09-06"
updated_at: "2026-09-06"
sources:
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/tLogistica e CS.tmdl"
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

# tLogistica e CS

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
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/tLogistica e CS.tmdl:54"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| Valor Logistica | Pendente | [Valor Logistica] | sum | não declarado | Não declarada | 4 |
| Valor CS | Pendente | [Valor CS] | sum | não declarado | Não declarada | 14 |
| order_sale_subtotal | Pendente | fVendas_unificada[order_sale_subtotal] | sum | não declarado | Não declarada | 24 |
| order_sale_quantity | Pendente | fVendas_unificada[order_sale_quantity] | sum | não declarado | Não declarada | 34 |
| order_sale_delivery_quantity | Pendente | fVendas_unificada[order_sale_delivery_quantity] | sum | não declarado | Não declarada | 43 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: tLogistica e CS-44de43b6-4baa-4b71-8bdf-2bcfb92032d0

Tipo: calculated. Propriedades: `{"mode": "import"}`. Fonte: linha 54.

```dax
CALCULATETABLE (
    SUMMARIZE (
        fVendas_unificada,
        fVendas_unificada[order_sale_subtotal],
        fVendas_unificada[order_sale_quantity],
        fVendas_unificada[order_sale_delivery_quantity],
        "Valor Logistica",(fVendas_unificada[order_sale_subtotal]/fVendas_unificada[order_sale_quantity]) * fVendas_unificada[order_sale_delivery_quantity],
        "Valor CS",(fVendas_unificada[order_sale_subtotal]/fVendas_unificada[order_sale_quantity]) * (fVendas_unificada[order_sale_quantity]-fVendas_unificada[order_sale_delivery_quantity])
    )
    ,fVendas_unificada[obt_sales_department_status] = "LOGISTICA E CS"
    ,fVendas_unificada[pedido_status] = "A FATURAR"
)
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 5 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 0. Consultar o [mapa do modelo](../../docs/ingestoes/2026-09-06-modelo-corporativo/modelo.md).

Medidas com referência direta:

- [00 Logística](<../../metrics/logistica/metrica_logistica.yaml>)
- [00 Customer Service](<../../metrics/comercial/metrica_customer_service.yaml>)

## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/tLogistica e CS.tmdl>)
