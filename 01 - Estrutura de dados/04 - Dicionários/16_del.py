# Remove as chaves de um dicionário com a palavra reservada del

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Remove a chave telefone do dicionário guilherme@gmail.com
del contatos["guilherme@gmail.com"]["telefone"]
# Remove a chave chappie@gmail.com do dicionário contatos
del contatos["chappie@gmail.com"]
# del contatos = apaga o dicioinário completo

# {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}  # noqa
print(contatos)
