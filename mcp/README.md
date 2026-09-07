# MCP Alexandria

Servidor MCP local, somente leitura, para expor os contratos governados do Atlas.

```sh
python -m pip install -r requirements.txt
python mcp/server.py
```

Tools: `search_alexandria`, `get_metric`, `get_dimension`, `get_dataset`,
`get_business_rule`, `get_concept` e `get_skill`.

O servidor devolve `authority=official` somente quando `status` e
`evidence_status` são `certified`. Ele não executa SQL/DAX, não acessa valores
atuais e não altera contratos. Para produção, publique o transporte aprovado pela
infraestrutura e conecte-o como MCP no Agente Alexandria do Copilot Studio.
