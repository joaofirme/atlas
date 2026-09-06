---
schema_version: 1
id: "regra_anatomia_nota"
title: "Anatomia da nota e proxies"
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
    locator: "medida Pedidos & Faturamentos HTML; linha 1188"
    accessed_at: "2026-09-06"
validation:
  reviewed_by: null
  reviewed_at: null
  evidence:
    - "Leitura estática do snapshot PBIP; sem execução ou certificação de negócio."
pending:
  - "Confirmar interpretação, responsáveis e comportamento com dados reais."
---

# Anatomia da nota e proxies

## Objetivo

O HTML chama de impostos a diferença positiva entre Receita Bruta e RSL. A largura visual dessa parcela tem piso de 18%.

## Definição e escopo

Interpretação documental da implementação observada na fonte de descoberta. Ainda não é uma definição certificada da empresa.

## Especificação

O piso é de apresentação, não alíquota. A diferença entre receitas não comprova a decomposição tributária. A variável vDevRefTotal soma devolução total e refaturamento; como devolução total já o inclui, há risco de duplicação dessa parcela na apresentação.

- [Pedidos & Faturamentos HTML](<../../metrics/corporativo/metrica_pedidos_e_faturamentos_html.yaml>)

## Exemplos

Usar a definição em perguntas sobre o indicador, sempre informando base de receita, empresa e período; não há resultados numéricos extraídos.

## Validação

Leitura estática; sem execução DAX, comparação numérica ou revisão de negócio.

## Dependências e impactos

Mudanças nessas definições podem afetar os visuais e cálculos dependentes listados em cada contrato.

## Pendências

Confirmar significado, responsáveis e uso oficial com a área.

## Fontes

- [Pedidos & Faturamentos HTML](<../../metrics/corporativo/metrica_pedidos_e_faturamentos_html.yaml>)
