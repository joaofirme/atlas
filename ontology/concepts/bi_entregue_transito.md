---
schema_version: 1
id: "bi_entregue_transito"
title: "Entregue e em trânsito"
type: "concept"
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
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida 06 Valor Entregue; linha 4236"
    accessed_at: "2026-09-06"
validation:
  reviewed_by: null
  reviewed_at: null
  evidence:
    - "Leitura estática do snapshot PBIP; sem execução ou certificação de negócio."
pending:
  - "Confirmar interpretação, responsáveis e comportamento com dados reais."
---

# Entregue e em trânsito

## Objetivo

Entregue usa data de entrega preenchida até hoje sobre faturamento. Em trânsito usa subtotal e janela por data de pedido; não presumir que somam o faturamento sem diferença.

## Definição e escopo

Interpretação documental da implementação observada no BI. Ainda não é uma definição certificada da empresa.

## Especificação

As expressões são mantidas nos contratos canônicos abaixo. Consultar também os filtros das páginas e as dependências transitivas.

- [06 Valor Entregue](<../../metrics/comercial/bi_06_valor_entregue.yaml>)

## Exemplos

Usar a definição em perguntas sobre o indicador, sempre informando base de receita, empresa e período; não há resultados numéricos extraídos.

## Validação

Leitura estática; sem execução DAX, comparação numérica ou revisão de negócio.

## Dependências e impactos

Mudanças nessas definições podem afetar os visuais e cálculos dependentes listados em cada contrato.

## Pendências

Confirmar significado, responsáveis e uso oficial com a área.

## Fontes

- [06 Valor Entregue](<../../metrics/comercial/bi_06_valor_entregue.yaml>)
