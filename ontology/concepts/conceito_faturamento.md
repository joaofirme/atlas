---
schema_version: 1
id: "conceito_faturamento"
title: "Faturamento"
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
    locator: "medida 00 Faturamento; linha 583"
    accessed_at: "2026-09-06"
validation:
  reviewed_by: null
  reviewed_at: null
  evidence:
    - "Leitura estática do snapshot PBIP; sem execução ou certificação de negócio."
pending:
  - "Confirmar interpretação, responsáveis e comportamento com dados reais."
---

# Faturamento

## Objetivo

Valor de receita de pedidos faturados/parciais por data de movimento. A origem declara desconto de IPI/ST; confirmar a transformação upstream.

## Definição e escopo

Interpretação documental da implementação observada na fonte de descoberta. Ainda não é uma definição certificada da empresa.

## Especificação

As expressões são mantidas nos contratos canônicos abaixo. Consultar também os filtros das páginas e as dependências transitivas.

- [00 Faturamento](<../../metrics/comercial/metrica_faturamento.yaml>)

## Exemplos

Usar a definição em perguntas sobre o indicador, sempre informando base de receita, empresa e período; não há resultados numéricos extraídos.

## Validação

Leitura estática; sem execução DAX, comparação numérica ou revisão de negócio.

## Dependências e impactos

Mudanças nessas definições podem afetar os visuais e cálculos dependentes listados em cada contrato.

## Pendências

Confirmar significado, responsáveis e uso oficial com a área.

## Fontes

- [00 Faturamento](<../../metrics/comercial/metrica_faturamento.yaml>)
