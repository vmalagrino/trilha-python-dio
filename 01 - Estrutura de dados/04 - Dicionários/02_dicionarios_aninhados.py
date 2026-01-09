contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a": 1}},
}

# Acessando dados de dicionários aninhados

# chave = giovanna@gmail.com, valor{ chave = telefone, valor = 3443-2121}
telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
# print valor
print(telefone)

nome = contatos["giovanna@gmail.com"]["nome"]  # "Giovanna"
# print valor
print(nome)

# Teste aninhamento extra

# mostra o que existe na chave melaine
teste1 = contatos["melaine@gmail.com"]
print(teste1)
# mostra o que existe na chave extra dentro da chave melaine
teste2 = contatos["melaine@gmail.com"]["extra"]
print(teste2)
# mostra o que existe na chave a dentro da chave extra dentro da chave melaine
teste3 = contatos["melaine@gmail.com"]["extra"]["a"]
print(teste3)
