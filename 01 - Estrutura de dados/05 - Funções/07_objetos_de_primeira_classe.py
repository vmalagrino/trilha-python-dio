# Tudo é objeto em Python, inclusive funções sendo tratadas como objetos de primeira classe.
# Podemos atribuir funções a variáveis, passá-las como parametros para outras funções
# Usar como valor em estrutura de dados (listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função (closures)

def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


# somar = passo o nome e não declaro os parênteses, para não executar a função
exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
