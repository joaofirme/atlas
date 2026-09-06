---
schema_version: 1
id: "regra_projecao_fechamento"
title: "Projeção, ritmo e gap"
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
    locator: "medida Farmax BI HTML v2; linha 5948"
    accessed_at: "2026-09-06"
validation:
  reviewed_by: null
  reviewed_at: null
  evidence:
    - "Leitura estática do snapshot PBIP; sem execução ou certificação de negócio."
pending:
  - "Confirmar interpretação, responsáveis e comportamento com dados reais."
---

# Projeção, ritmo e gap

## Objetivo

O painel executivo projeta fechamento a partir do ritmo por dia útil; o campo vGapProjetado, apesar do nome, calcula realizado menos meta.

## Definição e escopo

Interpretação documental da implementação observada na fonte de descoberta. Ainda não é uma definição certificada da empresa.

## Especificação

Variáveis: vRitmoAtualDU = receita / dias úteis realizados; vProjecaoFechamento = ritmo × dias úteis totais; vRitmoNecessarioDU = receita faltante / dias restantes. A projeção é extrapolação, não previsão estatística. Gap não usa a projeção nessa implementação. Sem meta, status SEM META.

- [Farmax BI HTML v2](<../../metrics/corporativo/metrica_farmax_bi_html_v2.yaml>)

## Exemplos

Usar a definição em perguntas sobre o indicador, sempre informando base de receita, empresa e período; não há resultados numéricos extraídos.

## Validação

Leitura estática; sem execução DAX, comparação numérica ou revisão de negócio.

## Dependências e impactos

Mudanças nessas definições podem afetar os visuais e cálculos dependentes listados em cada contrato.

## Pendências

Confirmar significado, responsáveis e uso oficial com a área.

## Fontes

- [Farmax BI HTML v2](<../../metrics/corporativo/metrica_farmax_bi_html_v2.yaml>)
