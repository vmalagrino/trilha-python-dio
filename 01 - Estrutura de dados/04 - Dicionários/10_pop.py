# Usando o método pop() para remover uma chave do dicionário e não sabe se o valor está no dicionário ou não

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# remove a chave e retorna o valor associado a ela
resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

# remove a chave e retorna o valor associado a ela, se a chave não existir, podemos retorna o valor padrão {} ou outro valor
resultado = contatos.pop("guilherme@gmail.com", "Não localizado")  # {}
print(resultado)
