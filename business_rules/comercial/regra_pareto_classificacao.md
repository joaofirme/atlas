---
schema_version: 1
id: "regra_pareto_classificacao"
title: "Classificação Pareto"
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
    locator: "medida Comercial HTML v1; linha 4003"
    accessed_at: "2026-09-06"
validation:
  reviewed_by: null
  reviewed_at: null
  evidence:
    - "Leitura estática do snapshot PBIP; sem execução ou certificação de negócio."
pending:
  - "Confirmar interpretação, responsáveis e comportamento com dados reais."
---

# Classificação Pareto

## Objetivo

O HTML calcula receita por cliente/grupo, ranking denso e participação acumulada; usa 80% para delimitar classe A.

## Definição e escopo

Interpretação documental da implementação observada na fonte de descoberta. Ainda não é uma definição certificada da empresa.

## Especificação

A implementação adiciona 1 ao número de clientes com participação acumulada até 80%. Rever empates, conjunto vazio, único cliente e a delimitação do cliente que cruza o limiar. O Top 15 exibido não corresponde necessariamente ao universo inteiro do Pareto.

- [Comercial HTML v1](<../../metrics/corporativo/metrica_comercial_html_v1.yaml>)

## Exemplos

Usar a definição em perguntas sobre o indicador, sempre informando base de receita, empresa e período; não há resultados numéricos extraídos.

## Validação

Leitura estática; sem execução DAX, comparação numérica ou revisão de negócio.

## Dependências e impactos

Mudanças nessas definições podem afetar os visuais e cálculos dependentes listados em cada contrato.

## Pendências

Confirmar significado, responsáveis e uso oficial com a área.

## Fontes

- [Comercial HTML v1](<../../metrics/corporativo/metrica_comercial_html_v1.yaml>)
