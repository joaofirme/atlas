# Atlas

Base de conhecimento de dados e negócio da Farmax, anteriormente MiniAlexandria. O Atlas documenta como indicadores são calculados, quais dados utilizam e como se relacionam, para uso por pessoas e agentes.

## Comece aqui

- [Avaliação da primeira fonte de descoberta](docs/ingestoes/2026-09-06-modelo-corporativo/avaliacao.md): cobertura, principais indicadores e pontos que precisam de revisão.
- [Catálogo de objetos](docs/catalogo.md): métricas, tabelas, dimensões, entidades, relacionamentos, conceitos e regras.
- [Inventário técnico da primeira fonte](docs/ingestoes/2026-09-06-modelo-corporativo/modelo.md): colunas, tipos, origem, transformações e relacionamentos observados.
- [Mapa conceitual](docs/ingestoes/2026-09-06-modelo-corporativo/ontologia.md): interpretação inicial do negócio encontrada na fonte.
- [Roadmap](docs/roadmap.md): próximas etapas.

## Estado atual

O Atlas cresce a partir dos artefatos que as áreas de negócio já usam e mantêm, como relatórios, modelos semânticos, consultas, planilhas e documentação. Eles aceleram a descoberta de métricas, tabelas, colunas, regras e relações, mas não definem a identidade canônica dos objetos no Atlas.

A primeira ingestão, realizada em 2026-09-06, mapeou 20 tabelas, 241 colunas, 90 medidas e 28 relacionamentos a partir de uma dessas fontes. Os nomes canônicos são independentes da ferramenta; a origem técnica permanece registrada somente para rastreabilidade.

Os contratos estão em `draft`. Uma definição observada em uma fonte é evidência de implementação ou uso, mas não comprova validação de negócio, qualidade dos dados ou equivalência com outros sistemas.

## Como contribuir

Agentes devem seguir [AGENTS.md](AGENTS.md) e a [skill de documentação](.agents/skills/atlas-documentation/SKILL.md). Consultar o catálogo antes de criar um objeto, preservar referências e separar o que está declarado, inferido e pendente.

Os arquivos YAML contêm os contratos canônicos e preservam as implementações observadas. Os documentos explicativos os referenciam sem copiar fórmulas. Veja a [decisão sobre fontes de descoberta](docs/decisoes/0001-fontes-existentes-como-aceleradores.md) antes de repetir ou ampliar uma extração.
