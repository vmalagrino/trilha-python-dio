# Função é um bloco de código nomeado (identificador) e pode receber uma lista de parâmetros que podem ou não ter valores padrões.
# Torna o código mais legível e reutilizável.
# Programar em funções é um dos pilares da programação estruturada.
# parametro = entrada de dados para a função/retorno = saída de dados da função

# def = indica o início da definição da função, o que vem após é o nome da função

def exibir_mensagem():
    print("Olá mundo!")

# nome sem valor, tenho que dar o valor ao executar a função
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

# nome com valor, posso ou não passar um valor ao executar a função
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

# exibe a mensagem Olá mundo!
exibir_mensagem()

# Passar um valor = O valor passado será considerado = "Victor"
# exibir_mensagem_2("Victor")
# exibir_mensagem_2(nome="Victor")
exibir_mensagem_2("Victor")

# Não passar um valor = O valor padrão definido ao criar a função = "Anônimo" será considerado
exibir_mensagem_3()

# Passar um valor = É ignorando o valor padrão "Anônimo" e considerado o valor passado "Giovanna"
# exibir_mensagem_3(nome="Giovanna")
exibir_mensagem_3("Giovanna")
