# issuperset verifica se um conjunto é um superconjunto de outro
# ou seja, se ele contém todos os elementos do outro conjunto

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# a contém todos os elementos de b? Não
resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

# b contém todos os elementos de a? Sim
resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)
