# Atlas

O Atlas é a fonte semântica governada de dados e negócio da Farmax. Ele registra, em Git, o significado dos indicadores, suas fórmulas e fontes, as dimensões válidas, os datasets recomendados, as regras de negócio, a ontologia corporativa e os procedimentos que orientam análises humanas ou realizadas por agentes de IA.

Este README é o ponto de entrada para o time de Dados. Ao terminar a leitura, você deve entender:

- qual problema o Atlas resolve;
- o que é e o que não é verdade oficial;
- como o repositório está organizado;
- como consultar, criar, revisar e certificar conteúdo;
- como as definições chegam a agentes por meio do MCP Alexandria;
- como executar as validações antes de abrir uma pull request.

## Por que o Atlas existe

Uma métrica não é apenas uma fórmula. Para ser reutilizada com segurança, ela também precisa declarar seu significado, unidade, granularidade, evento de tempo, filtros, dimensões compatíveis, fontes, regras e evidências de validação.

O Atlas centraliza esse contexto para responder perguntas como:

- O que significa Receita Líquida na Farmax?
- Qual é a diferença entre carteira aberta, total a faturar e programado?
- Qual dataset deve ser usado para analisar faturamento?
- Por quais dimensões uma métrica pode ser analisada?
- Qual regra define a data de referência?
- Onde a definição está implementada no Fabric ou Power BI?
- A informação foi apenas observada ou já foi certificada pelas áreas responsáveis?

O Git é a fonte oficial dos contratos semânticos. Sistemas como Spark, Redshift, Fabric e Power BI continuam sendo fontes, processadores ou implementações; não substituem a governança registrada aqui.

## Arquitetura

```text
 Fontes, documentos e implementações existentes
 Spark · Redshift · Fabric · Power BI · regras das áreas
                         │
                         │ evidências revisáveis
                         ▼
                  ATLAS NO GITHUB
          fonte semântica governada da Farmax
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
    Métricas         Dimensões          Datasets
       │                 │                 │
       └────────── Regras e ontologia ─────┘
                         │
                       Skills
                         │
                  Catálogos gerados
                         │
                         ▼
              MCP Alexandria read-only
                         │
                         ▼
       Agente Alexandria no Copilot Studio
                         │
                         ▼
                     Usuários
```

O Atlas não sincroniza automaticamente contratos com Fabric ou Power BI. Esses artefatos são referências de implementação e evidências da carga inicial. Mudanças no conteúdo governado passam por branch, validação, pull request e revisão humana.

## Princípios de governança

### Evidência não é certificação

Todo objeto possui duas classificações complementares:

| Campo | Valores | Significado |
|---|---|---|
| `status` | `draft`, `in_review`, `certified`, `deprecated` | Estado do contrato no fluxo de governança. |
| `evidence_status` | `observed`, `proposed`, `certified` | Nível de autoridade da informação registrada. |

- `observed`: informação encontrada em uma fonte, como TMDL, relatório ou documento. Não representa aprovação de negócio.
- `proposed`: definição proposta para avaliação.
- `certified`: definição revisada e aprovada, com responsáveis e evidências registradas.

Somente um objeto com `status: certified` e `evidence_status: certified` pode ser apresentado como verdade oficial. O MCP identifica os demais como `observed_not_official`.

### Certificação exige conteúdo completo

Os validadores bloqueiam a certificação incompleta. Dependendo do tipo, são exigidos:

- responsáveis de negócio e técnico;
- definição;
- unidade e granularidade;
- dimensões, datasets e regras relacionadas;
- fontes e evidências;
- revisor e data da revisão;
- mapeamento físico e linhagem;
- referências válidas para outros objetos do Atlas.

Uma validação estrutural aprovada não certifica um cálculo. DAX, SQL ou resultados numéricos somente são considerados validados quando executados e comparados no mesmo período, filtros, granularidade e tolerância.

### Rastreabilidade acima de inferência

Não invente tabelas, responsáveis, moedas, regras ou resultados. Quando uma informação ainda não estiver confirmada:

1. mantenha o objeto como `draft`;
2. classifique a evidência como `observed` ou `proposed`;
3. registre a fonte e o local exato da observação;
4. descreva a lacuna em `pending`;
5. identifique explicitamente compatibilidades que aguardam aprovação.

## Estrutura do repositório

Uma versão visual, com a árvore resumida e a mini documentação de cada pasta, está em [Estrutura do repositório Atlas](docs/estrutura-do-repositorio.md).

| Caminho | Conteúdo | Quando consultar |
|---|---|---|
| `metrics/` | Contratos canônicos de indicadores de negócio, organizados por domínio. | Para significado, fórmula, unidade, granularidade, filtros, dimensões, datasets, regras, fontes e implementações. |
| `dimensions/` | Dimensões analíticas, chaves, atributos, hierarquias e mapeamentos físicos. | Para saber como uma métrica pode ser segmentada e quais campos representam cliente, produto, tempo etc. |
| `datasets/` | Datasets orientados ao negócio e seus usos recomendados. | Para responder “qual dataset devo usar?” e rastrear o dataset até tabelas e modelos físicos. |
| `business_rules/` | Regras que definem condições, cálculos, exceções, datas ou classificações. | Quando o significado de uma métrica depende de uma regra corporativa. |
| `ontology/entities/` | Entidades do negócio e seus identificadores. | Para entender objetos como cliente, pedido, produto, faturamento ou devolução. |
| `ontology/relationships/` | Relações conceituais e joins físicos observados. | Para avaliar cardinalidade, direção, chaves, órfãos e risco de multiplicação de linhas. |
| `ontology/concepts/` | Vocabulário corporativo, sinônimos e diferenças entre conceitos próximos. | Para resolver ambiguidades de linguagem de negócio. |
| `skills/` | Procedimentos analíticos reutilizáveis por pessoas e agentes. | Para investigar uma pergunta seguindo métricas, dimensões e regras canônicas sem copiar fórmulas. |
| `.agents/skills/` | Instruções de manutenção do Atlas para LLMs e agentes. | Antes de criar, revisar ou reorganizar qualquer contrato. |
| `technical/measures/` | Medidas técnicas de apresentação, seletores, HTML, cores e auxiliares. | Para investigar implementação visual; não devem ser confundidas com indicadores de negócio. |
| `data_products/` | Inventário técnico legado das tabelas observadas na carga inicial. | Para auditoria de colunas e linhagem. O prefixo `tabela_` não significa produto de dados certificado. |
| `powerbi/` | Snapshot PBIP/TMDL usado como fonte de descoberta. | Somente para auditar fórmulas, tabelas, relações e configurações observadas. |
| `catalog/` | Índices JSON gerados para recuperação progressiva. | Para busca eficiente por agentes e integrações. Nunca editar manualmente. |
| `docs/` | Guias, decisões arquiteturais, roadmap, catálogos Markdown e registros de ingestão. | Para compreender contexto, decisões, pendências e navegação humana. |
| `mcp/` | Servidor MCP Alexandria somente leitura. | Para integrar os contratos do Atlas a agentes, incluindo Copilot Studio. |
| `scripts/` | Construção de catálogos, validação, consulta e ingestão documental. | Para operações locais e CI. Os scripts de ingestão não sincronizam contratos automaticamente. |
| `tests/` | Testes estruturais, de busca, referências, governança e links. | Antes de toda pull request e ao evoluir o formato dos contratos. |
| `.github/` | Workflow de CI e CODEOWNERS. | Para entender validações automáticas e responsabilidade de revisão por domínio. |
| `AGENTS.md` | Ponto de entrada obrigatório para agentes que trabalham no repositório. | Sempre que uma LLM ou agente iniciar uma consulta ou alteração. |

## Como os objetos se relacionam

```text
Métrica
  ├── usa outras métricas
  ├── pode ser analisada por → Dimensões
  ├── está disponível em → Datasets
  ├── é definida/restringida por → Business Rules
  ├── implementa ou materializa → Fabric/Power BI/objetos físicos
  └── é usada por → Skills analíticas

Dataset
  ├── recomenda métricas
  ├── expõe dimensões
  ├── aponta para implementação física
  └── preserva rastreabilidade para data_products/ e powerbi/
```

As ligações são feitas por IDs estáveis em `snake_case`. Não copie fórmulas canônicas para outros documentos: referencie o ID do contrato original.

## Formato comum dos contratos

Contratos YAML e frontmatter Markdown compartilham metadados básicos:

```yaml
schema_version: 1
id: identificador_estavel
title: Nome legível
type: metric
domain: comercial
status: draft
evidence_status: observed
version: 0.1.0
owners:
  business: null
  technical: null
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
sources:
  - reference: caminho ou identificação verificável
    locator: seção, linha ou trecho
    accessed_at: YYYY-MM-DD
validation:
  reviewed_by: null
  reviewed_at: null
  evidence: []
pending:
  - Informação que ainda precisa ser confirmada
```

O padrão completo para cada tipo está em [`.agents/skills/atlas-documentation/SKILL.md`](.agents/skills/atlas-documentation/SKILL.md). Essa é a referência normativa para manutenção.

## Como consultar

Para navegação humana:

- [guia de consulta](docs/consulta.md);
- [catálogo de negócio](docs/catalogo.md);
- [inventário técnico](docs/catalogo-tecnico.md);
- [roadmap](docs/roadmap.md).

Para busca local:

```sh
python -m pip install -r requirements.txt
python scripts/atlas.py search "qual dataset usar para vendas"
python scripts/atlas.py search "carteira aberta" --type metric
python scripts/atlas.py search "receita" --certified-only
python scripts/atlas.py show metrica_aberto
```

A busca é lexical, normaliza acentos e usa IDs, títulos, sinônimos e perguntas de negócio. Ela retorna candidatos e seus estados; não executa consultas nos dados.

## Como uma LLM deve trabalhar neste repositório

O arquivo [`AGENTS.md`](AGENTS.md) direciona a LLM para duas rotas:

- consultas devem começar por [`docs/consulta.md`](docs/consulta.md) e usar recuperação progressiva;
- alterações devem seguir integralmente [`.agents/skills/atlas-documentation/SKILL.md`](.agents/skills/atlas-documentation/SKILL.md).

Uma LLM mantenedora deve:

1. buscar por ID, nome e sinônimos antes de criar um objeto;
2. abrir somente os contratos e evidências necessários;
3. preservar IDs, fontes e conteúdo existente;
4. separar claramente observação, hipótese, proposta e aprovação;
5. usar português e IDs estáveis sem acentos;
6. registrar lacunas específicas em vez de preenchê-las por inferência;
7. referenciar contratos canônicos por ID;
8. executar build, validação e testes;
9. revisar o diff;
10. publicar por branch e pull request quando autorizada.

Rascunhos não podem ser respondidos como regras oficiais, e um agente não pode se declarar revisor de negócio.

## Como adicionar ou alterar conteúdo

1. Atualize sua cópia da `master` e crie uma branch.
2. Consulte o catálogo e confirme que o objeto não existe.
3. Leia a skill de manutenção.
4. Edite o contrato canônico correto.
5. Adicione fontes, evidências, referências e pendências.
6. Atualize a versão:
   - PATCH para esclarecimento sem mudança de significado;
   - MINOR para adição compatível;
   - MAJOR para mudança de fórmula, granularidade, filtro obrigatório ou contrato incompatível.
7. Para mudanças incompatíveis, registre decisão e impacto em `docs/decisoes/`.
8. Gere novamente os catálogos.
9. Execute todas as validações.
10. Revise o diff e abra uma pull request.

Mudanças em objetos certificados devem receber revisão de negócio e técnica. O [`CODEOWNERS`](.github/CODEOWNERS) contém a estrutura inicial de responsabilidade por domínio; os times definitivos ainda precisam ser configurados na organização GitHub.

## Validação local

Requer Python 3.10 ou superior.

```sh
python -m pip install -r requirements.txt
python scripts/atlas.py build
python scripts/atlas.py validate
python -m py_compile scripts/atlas.py mcp/server.py
python -m unittest discover -s tests
git diff --check
```

O build atualiza:

- `catalog/metrics.json`;
- `catalog/dimensions.json`;
- `catalog/datasets.json`;
- `catalog/concepts.json`;
- `catalog/business_rules.json`;
- `catalog/skills.json`;
- `docs/catalogo.md`;
- `docs/catalogo-tecnico.md`.

Se o build gerar diferenças, inclua os arquivos derivados na mesma pull request. O workflow em [`.github/workflows/validate.yml`](.github/workflows/validate.yml) repete essas verificações no GitHub.

## MCP Alexandria

O servidor em [`mcp/server.py`](mcp/server.py) oferece acesso somente leitura às definições:

- `search_alexandria`;
- `get_metric`;
- `get_dimension`;
- `get_dataset`;
- `get_business_rule`;
- `get_concept`;
- `get_skill`.

Execução local:

```sh
python mcp/server.py
```

O MCP não altera contratos, não executa DAX ou SQL e não acessa valores atuais. Para uso pelo Agente Alexandria no Copilot Studio, ainda é necessário publicar o transporte aprovado pela infraestrutura da Farmax e definir identidade, autenticação, rede, observabilidade e políticas de acesso.

## Fabric, Power BI, Spark e fontes físicas

- Spark e a arquitetura de engenharia atual permanecem preservados.
- Redshift e outras fontes físicas são registrados nos contratos quando confirmados.
- Fabric e Power BI são referências de implementação e evidência.
- Os arquivos PBIP/TMDL não certificam automaticamente uma definição de negócio.
- Os scripts de ingestão registram snapshots; não fazem sincronização automática.
- dbt e execução SQL não são o foco deste repositório.

O fluxo esperado é:

```text
implementação observada
        ↓
evidência registrada
        ↓
revisão de negócio e técnica
        ↓
contrato certificado no Atlas
```

## Limites atuais

- A maior parte do acervo inicial ainda está em `draft/observed`.
- O repositório não contém valores atuais dos indicadores.
- Não há execução de DAX ou SQL pelo MCP.
- Compatibilidades observadas entre métricas e dimensões ainda precisam de aprovação.
- O MCP existe localmente, mas ainda precisa ser publicado no ambiente corporativo.
- Os responsáveis por domínio no CODEOWNERS ainda devem evoluir para times reais da organização.
- A busca atual é lexical; busca semântica pode ser adicionada posteriormente sem mudar os contratos canônicos.

Consulte [`docs/roadmap.md`](docs/roadmap.md) para as próximas etapas de certificação, implantação e governança.

## Referências principais

- [Como consultar o Atlas](docs/consulta.md)
- [Padrão de manutenção](.agents/skills/atlas-documentation/SKILL.md)
- [Catálogo de negócio](docs/catalogo.md)
- [Inventário técnico](docs/catalogo-tecnico.md)
- [MCP Alexandria](mcp/README.md)
- [Decisões arquiteturais](docs/decisoes/)
- [Roadmap](docs/roadmap.md)
