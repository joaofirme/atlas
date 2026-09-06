---
name: atlas-documentation
description: Criar, revisar e organizar documentação, contratos semânticos e skills de análise no repositório Atlas, antiga MiniAlexandria da Farmax. Use ao cadastrar ou atualizar métricas, dimensões, ontologia, regras de negócio e produtos de dados, mantendo rastreabilidade e um padrão comum.
---

# Construção e documentação do Atlas

## Propósito e origem

Atlas é o nome atual da MiniAlexandria: uma base versionada de conhecimento de dados e negócio da Farmax, reutilizável por pessoas, BI e agentes. O objetivo é manter definições consistentes, explicar a origem dos dados e registrar como analisar cada domínio.

Fonte conceitual: conversa [Plataforma de IA do Ifood](https://chatgpt.com/c/6a98c0d7-4a88-83e9-9239-e6f3371c6df7), consultada em 2026-09-06. A conversa reúne um relato sobre o iFood e propostas de arquitetura para a Farmax; não comprova tabelas, fórmulas, responsáveis ou integrações em produção na Farmax. Não copiar a transcrição pessoal para a documentação.

Esta skill estabelece o padrão inicial do Atlas. Convenções de arquivos e metadados abaixo são decisões deste repositório, não especificações oficiais do iFood. Usar Atlas nos novos textos; preservar MiniAlexandria apenas como referência histórica.

## Arquitetura que vamos construir

- **Atlas/Git:** definições de negócio, contratos semânticos, documentação e procedimentos analíticos.
- **Redshift:** fonte de dados prevista no contexto; objetos físicos precisam ser confirmados.
- **Fabric/Power BI:** consumidores da definição de métricas; Atlas não substitui o modelo semântico.
- **Motor semântico futuro:** resolve métricas, dimensões, filtros e relacionamentos em consultas controladas.
- **API/MCP futuro:** permite a agentes descobrir e consultar o conhecimento do Atlas.
- **Agentes:** interpretam perguntas, escolhem procedimentos e explicam resultados com evidências.

O desenho final discutido evolui de recuperar SQL para consultar métricas por um contrato como `query_metric(metric, dimensions, filters)`. Tratar esses nomes como proposta de interface até existir implementação. O agente não deve inventar uma fórmula alternativa para uma métrica certificada.

O repositório não executa um servidor MCP por si só. Runtime, hospedagem, CI/CD e publicação no Fabric são etapas futuras, não capacidades instaladas pela criação desta documentação. A tecnologia do motor e o provedor de deploy permanecem em aberto.

## Organização do repositório

Criar diretórios somente quando houver conteúdo real para eles.

```text
atlas/
├── AGENTS.md
├── .agents/skills/atlas-documentation/SKILL.md
├── README.md                         # propósito, navegação e estado da construção
├── docs/
│   ├── catalogo.md                    # índice de objetos e status
│   ├── arquitetura/                   # desenho e limites das integrações
│   ├── decisoes/                      # decisões arquiteturais e migrações
│   └── roadmap.md                     # etapas, dependências e critérios de aceite
├── metrics/<dominio>/<id>.yaml
├── dimensions/<dominio>/<id>.yaml
├── ontology/
│   ├── entities/<id>.yaml
│   ├── relationships/<id>.yaml
│   └── concepts/<id>.md
├── business_rules/<dominio>/<id>.md
├── data_products/<dominio>/<id>.md
├── skills/<dominio>/<nome-da-skill>/SKILL.md
└── tests/                            # validações quando implementadas
```

`skills/` contém procedimentos analíticos do negócio; `.agents/skills/` contém a instrução de manutenção deste repositório. Não confundir as duas funções.

Usar português do Brasil nos textos. Usar IDs estáveis em `snake_case`, sem acentos; o nome do arquivo acompanha o ID. Pastas de skills e seu campo `name` usam `kebab-case`. Domínios iniciais possíveis: `logistica`, `comercial`, `financeiro`, `marketing`, `operacoes`; criar apenas os necessários.

Uma definição tem um único arquivo canônico. Documentos e skills referenciam esse arquivo por link relativo e ID, sem manter cópias de fórmulas. Separar uma variante em outro ID apenas quando representar outro significado de negócio.

## Fluxo de trabalho do agente documental

1. Ler as instruções do repositório, o catálogo e os arquivos relacionados, quando existirem. Inspecionar o estado Git antes de editar.
2. Identificar a solicitação, o domínio, o tipo de objeto e a fonte. Buscar por ID, nome e sinônimos antes de criar outro objeto.
3. Extrair definições confirmadas e separar propostas e lacunas. Não assumir que exemplos do chat são implementações reais.
4. Criar ou atualizar o arquivo canônico usando os contratos abaixo. Preservar IDs e registrar impactos nas referências dependentes.
5. Atualizar o catálogo e os links afetados. Na primeira contribuição de conteúdo, criar README e catálogo com links apenas para arquivos existentes.
6. Revisar consistência semântica e executar as validações disponíveis. Registrar o que foi efetivamente verificado e o que não pôde ser verificado.
7. Entregar um resumo com arquivos alterados, fontes, status, verificações e pendências. Se a tarefa incluir envio ao GitHub, seguir o fluxo de publicação abaixo.

Quando faltar informação, usar `null` no YAML e “Pendente de confirmação” no texto, com uma pendência específica. Listas vazias significam “nenhum item aplicável”, não “ainda não investigado”; usar `null` para desconhecido. Não preencher donos, tabelas ou resultados fictícios. Avançar no rascunho e pedir somente os dados que impedem a conclusão.

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

## Etapas de construção

1. **Base documental:** manter este padrão, criar navegação, catálogo e decisões. Aceite: outro agente encontra a regra e identifica onde cadastrar cada objeto.
2. **Piloto semântico:** logística é a proposta inicial da conversa. Confirmar domínio, responsáveis e fontes; documentar custo de frete, peso transportado, frete/kg e dependências reais. Aceite: definições revisadas, sem referências órfãs e com lacunas explícitas.
3. **Skill do piloto:** registrar o procedimento de análise de variação de frete e os exemplos de perguntas. Aceite: usa os IDs canônicos e possui saída e limitações claras.
4. **Validação automatizada:** implementar schemas, integridade referencial e testes semânticos. Aceite: erros de contrato impedem promoção, e resultados de testes ficam rastreáveis.
5. **Consumo programático:** implementar descoberta e leitura; evoluir para consultas controladas por motor semântico. Aceite: agente usa o contrato e os casos de erro são definidos. Não tratar Markdown sozinho como motor executável.
6. **Integração com Fabric:** definir escopo das medidas governadas, geração/publicação, comparação de versões, recuperação e testes de paridade. Aceite: mudanças preservam objetos fora do escopo e têm evidência de equivalência. Confirmar APIs e requisitos na documentação oficial na implementação.
7. **Expansão por domínio:** repetir o ciclo com novos produtos e métricas a partir da experiência do piloto.

Não construir runtime, infraestrutura ou centenas de objetos ao receber apenas uma solicitação documental. Atualizar o roadmap com evidência de cada etapa concluída.

## Revisão e publicação

Antes de finalizar uma contribuição, verificar:

- IDs únicos, nomes coerentes, links relativos válidos e dependências existentes; dependências ainda não criadas ficam como pendências explícitas.
- Metadados e campos particulares preenchidos ou marcados como desconhecidos; status compatível com a evidência.
- Ausência de fórmulas conflitantes, certificações inventadas e exemplos apresentados como dados reais.
- Granularidade, tempo, unidade e joins coerentes; SQL/DAX só marcados como testados quando executados e comparados.
- Nenhum segredo, credencial ou amostra identificável desnecessária incluído nos arquivos.
- Catálogo atualizado: ID, nome, tipo, domínio, status e link canônico para cada objeto novo ou alterado.

Executar os validadores do repositório quando existirem. Enquanto não existirem, realizar revisão documental e informar essa limitação; não afirmar que CI/CD ou testes automatizados passaram. Sem acesso aos dados, manter explícita a ausência de validação de execução.

Criar ou editar arquivos não implica deploy. Quando commit, push ou PR fizerem parte da solicitação autorizada, conferir branch e remote, incluir somente os arquivos da tarefa e usar uma mensagem como `docs(atlas): documenta frete por kg`. Para alterações de regras oficiais, preparar PR com mudança de negócio, fontes, impacto e validação para revisão dos responsáveis. Não sobrescrever histórico remoto nem fazer merge ou deploy por inferência da palavra “documentar”.

Ao atualizar integrações futuras, Atlas será a origem das definições sob sua gestão. Detectar e reconciliar divergências antes de publicar; não sobrescrever um modelo inteiro para alterar uma medida. Mudanças em medidas fora do escopo exigem uma decisão explícita de migração.

## Exemplo de solicitação

“Use a skill atlas-documentation para documentar a métrica frete por kg a partir destas fontes. Procure definições existentes, cadastre o contrato no domínio adequado, atualize o catálogo e informe as pendências. Mantenha como draft tudo que ainda não tiver validação.”
