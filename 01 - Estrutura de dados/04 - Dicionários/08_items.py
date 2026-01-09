# Usando o método items() para obter uma visão geral dos pares chave-valor em um dicionário

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.items()  # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})]) = itens do dicionpário([(chave, valor)])
print(resultado)
