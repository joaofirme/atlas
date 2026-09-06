---
schema_version: 1
id: "bi_estoque_valorizacao"
title: "Estoque e carteira por SKU"
type: "business_rule"
domain: "operacoes"
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
    locator: "medida Carteira e Estoque HTML v1; linha 2872"
    accessed_at: "2026-09-06"
validation:
  reviewed_by: null
  reviewed_at: null
  evidence:
    - "Leitura estática do snapshot PBIP; sem execução ou certificação de negócio."
pending:
  - "Confirmar interpretação, responsáveis e comportamento com dados reais."
---

# Estoque e carteira por SKU

## Objetivo

O HTML filtra demanda positiva e status diferente de INATIVO/DESCONTINUADO. Mostra os 20 SKUs por DemandaValor e seus subtotais.

## Definição e escopo

Interpretação documental da implementação observada no BI. Ainda não é uma definição certificada da empresa.

## Especificação

TicketMedio usa receita/quantidade de FATURADO na janela de 90 dias da maior data de pedido global, removendo filtros. EstoqueCalculadoValor = estoque × ticket; DemandaValor = demanda × ticket; EstoqueTotalValor acrescenta A Faturar. Não equivale automaticamente a estoque físico ou valorização contábil. O subtotal se refere ao Top 20, não a todos os SKUs.

- [Carteira e Estoque HTML v1](<../../metrics/corporativo/bi_carteira_e_estoque_html_v1.yaml>)

## Exemplos

Usar a definição em perguntas sobre o indicador, sempre informando base de receita, empresa e período; não há resultados numéricos extraídos.

## Validação

Leitura estática; sem execução DAX, comparação numérica ou revisão de negócio.

## Dependências e impactos

Mudanças nessas definições podem afetar os visuais e cálculos dependentes listados em cada contrato.

## Pendências

Confirmar significado, responsáveis e uso oficial com a área.

## Fontes

- [Carteira e Estoque HTML v1](<../../metrics/corporativo/bi_carteira_e_estoque_html_v1.yaml>)
