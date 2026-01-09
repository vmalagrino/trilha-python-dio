# Usando o método get() para acessar valores de um dicionário sem gerar erro caso a chave não exista
# Verifica se a chave existe, se existir retorna o valor, se não existir retorna None ou um valor padrão definido

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

# Existe a chave "teste" Não = None
resultado = contatos.get("teste")  # None
print(resultado)

# Existe a chave "teste"? Não = None, porém ele retorna um dicionário vazio ao invés de None se usar {} = valor default
resultado = contatos.get("teste", {})  # {}
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)
