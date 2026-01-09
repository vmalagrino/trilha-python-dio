# Usando o método copy() para copiar um dicionário e poder alterar a cópia, visualmente igual mas o ID é diferente

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Victor"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}
print(id(contatos))

print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}
print(id(copia))
