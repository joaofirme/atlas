---
schema_version: 1
id: "bi_pareto_clientes"
title: "Pareto de clientes"
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

# Pareto de clientes

## Objetivo

Receita por grupo de cliente é ordenada para calcular concentração. A regra observada para classe A conta acumulados até 80% e adiciona 1; confirmar empates e limites.

## Definição e escopo

Interpretação documental da implementação observada no BI. Ainda não é uma definição certificada da empresa.

## Especificação

As expressões são mantidas nos contratos canônicos abaixo. Consultar também os filtros das páginas e as dependências transitivas.

- [Comercial HTML v1](<../../metrics/corporativo/bi_comercial_html_v1.yaml>)

## Exemplos

Usar a definição em perguntas sobre o indicador, sempre informando base de receita, empresa e período; não há resultados numéricos extraídos.

## Validação

Leitura estática; sem execução DAX, comparação numérica ou revisão de negócio.

## Dependências e impactos

Mudanças nessas definições podem afetar os visuais e cálculos dependentes listados em cada contrato.

## Pendências

Confirmar significado, responsáveis e uso oficial com a área.

## Fontes

- [Comercial HTML v1](<../../metrics/corporativo/bi_comercial_html_v1.yaml>)
