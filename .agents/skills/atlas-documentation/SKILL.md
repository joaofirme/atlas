---
name: atlas-documentation
description: Manter contratos, documentação e procedimentos analíticos do Atlas com rastreabilidade.
---

# Manutenção do Atlas

O Atlas é a base de conhecimento de dados e negócio da Farmax. Esta skill é para edição; consultas seguem [docs/consulta.md](../../../docs/consulta.md).

## Organização e leitura

- `metrics/`: indicadores de negócio; uma definição e uma implementação canônica por ID.
- `dimensions/`, `ontology/` e `business_rules/`: dimensões, entidades, joins, conceitos e regras referenciáveis.
- `skills/`: procedimentos analíticos; `.agents/skills/`: instruções de manutenção.
- `technical/measures/`: seletores, HTML, cores, placeholders e adaptações visuais. Preservar IDs para dependências.
- `data_products/`: documentação técnica legada de tabelas; o prefixo `tabela_` não comprova produto governado.
- `catalog/metrics.json`: índice de busca gerado; não editar à mão nem copiar fórmulas para ele.
- `powerbi/` e `docs/ingestoes/`: evidências; ler somente quando houver necessidade de auditar a origem.
- `docs/catalogo.md` e `docs/catalogo-tecnico.md`: índices gerados por tipo de consulta.

## Fluxo de edição

1. Conferir Git e buscar por ID, nome e sinônimos antes de criar um objeto. Abrir apenas os contratos relacionados.
2. Usar português e IDs estáveis em snake_case sem acentos. Skills usam pastas e name em kebab-case. Criar pastas apenas com conteúdo real.
3. Separar implementação observada, hipótese e aprovação de negócio. Fontes podem ser relatórios, modelos, SQL, planilhas e APIs; nomes de negócio não dependem da ferramenta.
4. Não inventar tabelas, moeda, responsáveis, certificação ou resultados. Registrar lacunas específicas. SQL/DAX só são testados após execução comparada.
5. Preservar evidência, dependências e IDs; uma fórmula canônica não deve ser copiada para textos ou índices. Remover repetição literal; preservar divergências entre descrição e expressão.
6. Executar `python scripts/atlas.py build`, `python scripts/atlas.py validate` e `python -m unittest discover -s tests`. Revisar links e diff. Os testes estruturais não certificam cálculos.
7. Se autorizado, publicar somente arquivos da tarefa no branch/remote conferidos, sem force push. Mudanças de regras certificadas exigem PR para revisão de negócio.

Os scripts `document_powerbi.py` e `map_powerbi_semantics.py` registram a carga inicial; não são sincronizadores de contratos curados. Para nova ingestão, comparar evidências antes de editar.

## Metadados comuns

Todo objeto de conteúdo, em YAML ou frontmatter Markdown, usa:

```yaml
schema_version: 1
id: identificador_estavel
title: Nome legível
type: metric
domain: logistica
status: draft
version: 0.1.0
owners:
  business: null
  technical: null
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
sources:
  - reference: "URL, caminho do documento ou identificação verificável da fonte"
    locator: "Seção, mensagem ou trecho relevante"
    accessed_at: YYYY-MM-DD
validation:
  reviewed_by: null
  reviewed_at: null
  evidence: []
pending:
  - "Informação específica que precisa ser confirmada"
```

Substituir os valores ilustrativos ao criar um objeto. `type` aceita `metric`, `dimension`, `entity`, `relationship`, `concept`, `business_rule`, `data_product` ou `analysis_skill`. Documentos de navegação e esta skill de manutenção não precisam desse frontmatter.

Estados: `draft` (incompleto ou proposto), `in_review` (pronto para revisão), `certified` (aprovação de negócio e validação técnica registradas), `deprecated` (substituído ou retirado, com motivo e sucessor quando existir). O agente não se declara revisor de negócio. Rascunhos não podem ser apresentados como regras oficiais. Uma alteração de significado em objeto certificado retorna a revisão.

Versionamento do conteúdo: PATCH para esclarecimento sem mudança de significado; MINOR para adição compatível; MAJOR para mudança de cálculo, granularidade, filtro obrigatório ou contrato incompatível. Registrar a justificativa e o impacto de mudanças incompatíveis em `docs/decisoes/`. `schema_version` identifica o formato do contrato e é independente da versão do conteúdo.

## Contrato de métricas

Acrescentar aos metadados comuns:

- `definition`: significado de negócio, com inclusões e exclusões.
- `business_questions` e `synonyms`: perguntas atendidas e nomes pelos quais a métrica é conhecida.
- `unit`: moeda, percentual, quantidade ou unidade física, sem confundir formato visual com unidade.
- `grain`: o que uma linha de origem representa; registrar também a granularidade de cálculo quando diferente.
- `time`: campo de data, evento de referência, calendário, fuso e regra de fechamento pertinentes.
- `formula`: expressão conceitual e IDs de métricas dependentes.
- `aggregation`: agregação válida e restrições de aditividade por dimensão e tempo.
- `dimensions`: IDs das dimensões permitidas; `relationships`: IDs dos caminhos de join aprovados.
- `filters`: filtros obrigatórios, opcionais e exclusões, incluindo cancelamentos ou devoluções quando aplicáveis.
- `data_sources`: objetos físicos e colunas confirmados, vinculados às evidências de origem.
- `implementations`: SQL/DAX confirmados, dialeto, dependências e limitações; `null` enquanto não confirmados.
- `edge_cases`: nulos, divisão por zero, duplicidades, dados atrasados e arredondamento pertinentes.
- `checks`: casos de validação, resultado esperado e evidência da execução, quando houver.

Uma métrica derivada referencia outras métricas pelo ID. Razões exigem definir a agregação: razão de somas e média de razões não são intercambiáveis. Não declarar limites universais como margem menor que 100% sem regra de negócio confirmada.

Exemplo conceitual para um futuro rascunho `frete_por_kg`: custo de frete dividido pelo peso transportado. Ainda será necessário confirmar os componentes de custo, unidade do peso, granularidade, datas, filtros e tabelas. O exemplo `gold.fato_entregas` do chat não constitui evidência de que essa tabela existe. Não cadastrar esse exemplo como certificado.

Quando SQL e DAX coexistirem, ambos implementam a mesma definição. A equivalência depende de testes com o mesmo período, filtros, granularidade, tratamento de nulos e tolerância declarada; sem isso, registrar como não validada.

## Contratos dos demais conteúdos

| Tipo | Conteúdo obrigatório além dos metadados |
|---|---|
| Dimensão | Definição, entidade vinculada, chave, atributos, hierarquia se houver, mapeamento físico, valores desconhecidos, comportamento histórico e métricas compatíveis. |
| Entidade | Significado no negócio, identificador, granularidade, atributos e mapeamentos físicos confirmados. |
| Relacionamento | Entidades de origem/destino, verbo de negócio, cardinalidade e direcionalidade; separar relação conceitual do join físico. Para join: chaves, tipo, tratamento de órfãos e risco de multiplicação de linhas. |
| Conceito | Definição, sinônimos, exemplos, diferenças em relação a conceitos próximos e objetos relacionados. |
| Regra de negócio | Contexto, condição, ação ou cálculo, exceções, vigência, autoridade da regra e objetos impactados. |
| Produto de dados | Objetivo, consumidores, entradas/saídas, granularidade, linhagem, dependências, atualização, qualidade, acesso e sustentação. SLAs somente se acordados. |
| Skill analítica | Quando usar, entradas, pré-condições, métricas/dimensões/regras por ID e link, sequência analítica, verificações, limites e formato de resposta. |

Para conteúdos Markdown usar, nesta ordem: `# Título`, `## Objetivo`, `## Definição e escopo`, `## Especificação`, `## Exemplos`, `## Validação`, `## Dependências e impactos`, `## Pendências`, `## Fontes`. Em `Especificação`, incluir os campos particulares do tipo. Explicitar “Não se aplica” com motivo quando necessário.

Para skills analíticas, manter no frontmatter os campos nativos `name` e `description`; colocar os metadados comuns dentro de `metadata`. Usar no corpo: `Quando usar`, `Entradas e pré-condições`, `Referências canônicas`, `Procedimento`, `Validação`, `Formato de saída`, `Limites e pendências` e `Fontes`. Não reproduzir fórmulas de arquivos canônicos.

Uma resposta analítica deve informar período, filtros, métricas utilizadas, comparação, resultados, evidências e limitações. Separar observação de hipótese causal. Por exemplo, a skill de frete pode investigar volume, mix e tarifa, mas não deve alegar causalidade sem evidência ou inventar uma decomposição matemática.
