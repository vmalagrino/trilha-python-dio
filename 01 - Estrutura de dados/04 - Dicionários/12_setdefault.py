contato = {"nome": "Guilherme", "telefone": "3333-2221"}

# se a chave "nome" existir, retorna o valor associado a ela; se não existir, adiciona a chave com o valor "Giovanna"
contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

# se a chave "idade" não existir, adiciona a chave com o valor 28
contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
