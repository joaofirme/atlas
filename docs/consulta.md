# Consultar o Atlas

1. Localize o objeto por nome, sinônimos ou pergunta nos índices de `catalog/`. Com execução local, prefira a busca abaixo: ela retorna candidatos sem carregar contratos completos no contexto do agente.
2. Abra o contrato escolhido. Diferencie variantes antes de consultar valores. Preserve status, filtros, evento de data, unidade e limites.
3. Use `show` para obter referências das dependências, impactos, dimensões candidatas, relacionamentos observados e páginas do relatório. Abra apenas o necessário; referências transitivas não comprovam exibição nem causalidade.
4. Para calcular, a integração precisa acessar o modelo/dados com permissões e contexto equivalentes. O Atlas não fornece valores atuais nem executa DAX/SQL. Sem conexão, explique a definição e a lacuna, sem inventar um número.
5. Para explicar variações, siga a skill analítica do assunto e cite evidências numéricas. Dependência de fórmula é impacto matemático; não é causa operacional comprovada.

## Busca local

Requer Python 3.10+ e `pip install -r requirements.txt`, executados na raiz.

```sh
python scripts/atlas.py search "quanto de receita a faturar estão abertas"
python scripts/atlas.py show metrica_aberto
```

Os índices são derivados dos contratos: `python scripts/atlas.py build`. A busca cobre métricas, dimensões, datasets, conceitos, regras e skills. Use `--type dataset` para restringir e `--certified-only` quando o consumidor precisar apenas de definições oficiais.

O servidor em `mcp/server.py` expõe busca e leitura por tipo. Em produção, transporte, identidade e autenticação devem ser publicados pela infraestrutura antes da conexão com o Copilot Studio.

## Exemplo: receita a faturar em aberto

| Intenção | Contrato |
|---|---|
| Carteira com programação até hoje | [Carteira aberta](../metrics/comercial/metrica_aberto.yaml) |
| Toda a carteira a faturar, inclusive futura | [Total a faturar](../metrics/comercial/metrica_total_a_faturar.yaml) |
| Programação posterior a hoje | [Carteira programada](../metrics/comercial/metrica_programado.yaml) |

“Em aberto” também pode significar toda a carteira na linguagem da área. Se o contexto não resolver, esclarecer esse escopo antes de retornar um valor. Consulte o [procedimento de análise](../skills/comercial/analisar-carteira/SKILL.md).

## Leitura sob demanda

- Contratos: cálculo, fontes, pendências e dependências.
- Dimensões e relacionamentos: atributos, chaves e riscos; compatibilidade ainda depende de validação.
- [Catálogo técnico](catalogo-tecnico.md): tabelas e cálculos de apresentação.
- `powerbi/` e `docs/ingestoes/`: fonte original e inventários para auditoria, filtros e detalhes de visual. Não incluir por padrão em contexto ou recuperação de negócio.

O consumo de tokens depende do que a integração recupera. Manter evidências no Git não obriga o agente a lê-las; o conector deve respeitar essa seleção progressiva.
