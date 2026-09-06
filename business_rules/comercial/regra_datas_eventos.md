---
schema_version: 1
id: "regra_datas_eventos"
title: "Datas dos eventos"
type: "business_rule"
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
    locator: "medida 00 Valor de Vendas; linha 637"
    accessed_at: "2026-09-06"
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida 00 Faturamento; linha 583"
    accessed_at: "2026-09-06"
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida 02 Cancelado; linha 5280"
    accessed_at: "2026-09-06"
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida 04 Aberto; linha 472"
    accessed_at: "2026-09-06"
validation:
  reviewed_by: null
  reviewed_at: null
  evidence:
    - "Leitura estática do snapshot PBIP; sem execução ou certificação de negócio."
pending:
  - "Confirmar interpretação, responsáveis e comportamento com dados reais."
---

# Datas dos eventos

## Objetivo

Pedido usa a relação padrão com data_pedido; faturamento ativa data_movimento. Cancelamento FARMAX usa sale_cancellation_date, SANAVITA usa data_pedido. A carteira pendente remove filtros de dTempo.

## Definição e escopo

Interpretação documental da implementação observada na fonte de descoberta. Ainda não é uma definição certificada da empresa.

## Especificação

Não comparar indicadores como se todos representassem eventos ocorridos no mesmo período. Registrar o evento de cada parcela e os filtros adicionais do visual.

- [00 Valor de Vendas](<../../metrics/comercial/metrica_valor_de_vendas.yaml>)
- [00 Faturamento](<../../metrics/comercial/metrica_faturamento.yaml>)
- [02 Cancelado](<../../metrics/comercial/metrica_cancelado.yaml>)
- [04 Aberto](<../../metrics/comercial/metrica_aberto.yaml>)

## Exemplos

Usar a definição em perguntas sobre o indicador, sempre informando base de receita, empresa e período; não há resultados numéricos extraídos.

## Validação

Leitura estática; sem execução DAX, comparação numérica ou revisão de negócio.

## Dependências e impactos

Mudanças nessas definições podem afetar os visuais e cálculos dependentes listados em cada contrato.

## Pendências

Confirmar significado, responsáveis e uso oficial com a área.

## Fontes

- [00 Valor de Vendas](<../../metrics/comercial/metrica_valor_de_vendas.yaml>)
- [00 Faturamento](<../../metrics/comercial/metrica_faturamento.yaml>)
- [02 Cancelado](<../../metrics/comercial/metrica_cancelado.yaml>)
- [04 Aberto](<../../metrics/comercial/metrica_aberto.yaml>)
