---
schema_version: 1
id: "conceito_carteira_aberta"
title: "Carteira aberta"
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

# Carteira aberta

## Objetivo

A faturar com programação até hoje, independentemente do filtro de calendário removido pela medida base. Não equivale a toda a carteira pendente.

## Definição e escopo

Interpretação documental da implementação observada na fonte de descoberta. Ainda não é uma definição certificada da empresa.

## Especificação

As expressões são mantidas nos contratos canônicos abaixo. Consultar também os filtros das páginas e as dependências transitivas.

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

- [04 Aberto](<../../metrics/comercial/metrica_aberto.yaml>)
