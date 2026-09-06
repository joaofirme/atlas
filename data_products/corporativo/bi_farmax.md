---
schema_version: 1
id: bi_farmax
title: "BI corporativo Farmax"
type: data_product
domain: corporativo
status: draft
version: "0.1.0"
owners:
  business: null
  technical: null
created_at: "2026-09-06"
updated_at: "2026-09-06"
sources:
  - reference: "powerbi/Farmax v3 (1).pbip"
    locator: "projeto PBIP e artefatos Report/SemanticModel referenciados"
    accessed_at: "2026-09-06"
  - reference: "Solicitação do usuário no projeto Atlas"
    locator: "Uso do dashboard pelos times para acompanhar indicadores da empresa"
    accessed_at: "2026-09-06"
validation:
  reviewed_by: null
  reviewed_at: null
  evidence:
    - "Inventário estático: 20 tabelas, 241 colunas, 90 medidas, 28 relacionamentos e 6 páginas."
pending:
  - "Identificar responsáveis, SLA, usuários e ambiente publicado."
  - "Revisar as divergências de semântica e referências documentadas."
---

# BI corporativo Farmax

## Objetivo

Acompanhar indicadores da empresa pelos times, conforme o uso informado pelo usuário. O snapshot reúne vendas, faturamento, devoluções, metas, carteira, estoque e análises comerciais.

## Definição e escopo

Projeto local Farmax v3 (1), composto de relatório e modelo semântico. A exportação não comprova que corresponda à versão atualmente publicada no serviço.

## Especificação

- Entradas: Redshift, entidades de dataflows e tabelas locais/calculadas.
- Saídas: Painel Executivo, duas páginas chamadas Pedidos & Faturamento, Carteira & Estoque, Comercial e Testes.
- Granularidade: varia por fato; não existe uma granularidade única para todo o produto.
- Atualização: partições e timestamp local documentados; agenda no serviço e SLA pendentes.
- Acesso: quatro roles de leitura, sem filtros RLS declarados nos arquivos; atribuições no serviço desconhecidas.
- Sustentação: responsáveis e rotina de incidentes pendentes.

## Exemplos

Perguntas atendidas pelo desenho: quanto foi vendido/faturado; qual o atingimento da meta; onde estão as pendências da carteira; como clientes, marcas e regionais participam da receita; quais SKUs exigem atenção de estoque. Respostas numéricas não foram coletadas nesta ingestão.

## Validação

Documentação em rascunho. Não houve execução do dashboard, consulta a registros ou certificação de métricas.

## Dependências e impactos

[Catálogo](../../docs/catalogo.md), [modelo e linhagem](../../docs/powerbi/modelo.md), [páginas e visuais](../../docs/powerbi/paginas.md) e [avaliação](../../docs/powerbi/avaliacao.md). Alterações em medidas base propagam para matrizes e para cálculos internos de HTML.

## Pendências

Confirmar responsáveis, versão publicada, qualidade, granularidades, chaves e regras tributárias upstream. Priorizar os achados descritos na avaliação antes de promover objetos a certificados.

## Fontes

[Projeto PBIP](<../../powerbi/Farmax v3 (1).pbip>) e [manifesto de arquivos de origem](../../docs/powerbi/manifesto_fontes.json).
