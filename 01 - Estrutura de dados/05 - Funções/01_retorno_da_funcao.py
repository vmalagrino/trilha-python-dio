# Para retornar um valor, utilizamos a palavra reservada "return". Toda função Python retorna None por padrão
# Python pode retornar mais de um valor, outras linguagens não.

def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)

def soma(a, b):
    return a + b
print(soma(2, 9))  # 5
