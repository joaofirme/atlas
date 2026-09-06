# Organização para consulta progressiva

Data: 2026-09-06. Escopo: organização e descoberta; sem alteração de fórmulas ou certificação.

## Avaliação

A carga inicial colocou 90 medidas no mesmo catálogo: 57 indicadores e 33 auxiliares visuais, medidas de exibição, seletores, placeholders e renderizações HTML. O README direcionava primeiro à avaliação da ingestão. Muitos contratos repetiam literalmente a descrição da fonte; perguntas de negócio estavam vazias e os sinônimos preservavam apenas o nome técnico.

Ler HTML, inventários completos e planejamento antes de localizar a métrica aumenta o contexto sem resolver a pergunta. IDs de joins opacos e `usage: []` em medidas base também dificultavam descobrir dimensões e usos indiretos no relatório.

## Plano aplicado

1. Entrada curta para consulta, separada das instruções de manutenção e do histórico de ingestão.
2. Separação das 33 medidas técnicas em `technical/measures/`, preservando IDs e referências; catálogos de negócio e técnico gerados separadamente.
3. Remoção de `source_description` somente quando idêntico a `definition`. Divergências e expressões originais permanecem auditáveis. Remoção de arquitetura especulativa e história pessoal da skill de manutenção.
4. Busca curta gerada dos 57 contratos de indicadores; nomes e sinônimos de carteira enriquecidos. Expansão sob demanda com dependências reversas, usos transitivos em páginas e dimensões candidatas por tabelas e joins observados.
5. Primeiro procedimento analítico para carteira, com critérios de comparação e limites causais.
6. Validação automática de IDs, dependências, ciclos, links e recuperação do exemplo; publicação no Git.

## Decisões de preservação

Fontes PBIP/TMDL, inventários, conceitos e regras permanecem porque contêm evidências únicas. Não foram apagados por tamanho. Os contratos `data_products/tabela_*` são inventário técnico legado; não foram promovidos a produtos de negócio. O catálogo técnico deixa essa distinção explícita.

O formato dos contratos mantém campos desconhecidos: remover `null` indiscriminadamente ocultaria lacunas importantes para consultas. `dimensions: null` continua desconhecido; a descoberta automática retorna candidatos separadamente, sem inventar joins aprovados.

## Limites e próximos passos

A busca é local e lexical. Ainda é necessário ampliar sinônimos dos demais indicadores com a área, revisar unidade e granularidade, confirmar joins e ligar uma ferramenta de consulta ao modelo ou banco. Páginas são identificadas pelo snapshot local; URLs do serviço publicado não foram fornecidas. Há procedimento para investigar variação, mas não dados para provar uma causa.

Comparar custos pela quantidade de conteúdo efetivamente retornado por busca/expansão, não pelo tamanho total do Git. Nenhuma contagem de tokens de modelo é presumida a partir de bytes.

## Verificação desta mudança

- 190 objetos carregados; IDs únicos, dependências existentes e ausência de ciclos verificados.
- As 90 implementações originais, seus IDs, estados e dependências de fórmula foram comparados com o Git anterior e preservados.
- Seis testes locais cobrem integridade, busca e ambiguidade, exclusão de apresentação da busca, índice atualizado, contexto transitivo, rejeição de dependências inválidas e links Markdown.
- A pergunta de exemplo retorna `metrica_aberto` primeiro. A expansão identifica as páginas “Carteira & Estoque” e “Pedidos & Faturamento”, com evidência dos visuais e ressalva de uso transitivo.
- Workflow adicionado para repetir verificações no GitHub; a execução remota não faz parte das evidências locais acima. Não houve execução DAX/SQL nem validação numérica de negócio.
