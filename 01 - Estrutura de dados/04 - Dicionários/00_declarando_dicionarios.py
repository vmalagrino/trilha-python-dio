# Um dicionário é um conjunto não-ordenado de pares chave:valor.
# Onde as chaves são únicas em uma dada instancia do dicionário.
# São delimitados por chaves: {}, e contém uma lista de pares chave:valor separada por vírgulas.
# chave válida = valor imutável (string, número, tupla)
# valor pode ser qualquer tipo imutavel ou mutável (string, número, tupla, lista, dicionário, etc).
# se a chave for repetida, o último valor atribuído à chave será o mantido no dicionário.


# primeira forma de declarar um dicionário
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

# segunda forma de declarar um dicionário
pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

# adicionando novos pares chave:valor = variavel[chave] = valor
pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)
