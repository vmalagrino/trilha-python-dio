# issubset verifica se um conjunto é subconjunto de outro

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# a é um subconjunto de b? Sim pois todos os elementos de a estão em b
resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

# b é um subconjunto de a? Não pois nem todos os elementos de b estão em a
resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)