# Usando o método update() para atualizar uma chave existente ou adicionar uma nova chave

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.update({"guilherme@gmail.com": {"nome": "Gui", "telefone": "2221"}})
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui', 'telefone': '2221'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)
