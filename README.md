# Atlas

Base de conhecimento de dados e negócio da Farmax, anteriormente MiniAlexandria. O Atlas documenta como indicadores são calculados, quais dados utilizam e como se relacionam, para uso por pessoas e agentes.

## Comece aqui

- [Avaliação da primeira ingestão do Power BI](docs/powerbi/avaliacao.md): cobertura, principais indicadores e pontos que precisam de revisão.
- [Catálogo de objetos](docs/catalogo.md): métricas, tabelas, dimensões, entidades, relacionamentos, conceitos e regras.
- [Modelo e dicionário de tabelas](docs/powerbi/modelo.md): colunas, tipos, origem, transformações e relacionamentos.
- [Páginas do dashboard](docs/powerbi/paginas.md): vínculo entre visuais e medidas.
- [Mapa conceitual](docs/powerbi/ontologia.md): interpretação inicial do negócio representado no BI.
- [Roadmap](docs/roadmap.md): próximas etapas.

## Estado atual

A primeira fonte é o projeto `Farmax v3 (1)` em `powerbi/`, informado pelo usuário como dashboard utilizado pelos times para acompanhar os indicadores da empresa. A ingestão de 2026-09-06 mapeou 20 tabelas, 241 colunas, 90 medidas, 28 relacionamentos e 6 páginas com 65 visuais.

Os contratos estão em `draft`. A definição observada no Power BI é evidência de implementação, mas não comprova validação de negócio, qualidade dos dados ou equivalência com outro sistema. Não houve consulta ao Redshift, execução do modelo ou extração de linhas do cache local.

## Como contribuir

Agentes devem seguir [AGENTS.md](AGENTS.md) e a [skill de documentação](.agents/skills/atlas-documentation/SKILL.md). Consultar o catálogo antes de criar um objeto, preservar referências e separar o que está declarado, inferido e pendente.

Os arquivos YAML contêm as expressões canônicas importadas. Os documentos explicativos as referenciam. As fontes originais em `powerbi/` foram preservadas; este trabalho não modifica o dashboard. Veja a [decisão sobre esta ingestão](docs/decisoes/0001-ingestao-powerbi.md) antes de repetir a extração.
