# Usando o método popitem() para remover os itens em sequência

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# não informamos qual a chave e ele retira os itens na sequência
resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)

# Se não existir mais itens para remover, gera erro
# contatos.popitem()  # KeyError
