# Checamos se uma chave existe em nosso dicionário com o método in

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# a chave existe no dicionário contatos?
resultado = "guilherme@gmail.com" in contatos  # True
print(resultado)

# a chave existe no dicionário contatos?
resultado = "megui@gmail.com" in contatos  # False
print(resultado)

# a chave existe no dicionário contatos?
resultado = "idade" in contatos["guilherme@gmail.com"]  # False
print(resultado)

# a chave existe no dicionário contatos?
resultado = "telefone" in contatos["giovanna@gmail.com"]  # True
print(resultado)

# incluir o not a frente de in torna a pergunta na negativa