# intersection retorna a interseção entre dois conjuntos = 2,3

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_c = {3, 4, 5}

# o que é igual em a e b
resultado = conjunto_a.intersection(conjunto_b)
print(resultado)

# o que é igual em a, b e c
resultado = conjunto_a.intersection(conjunto_b).intersection(conjunto_c)
print(resultado)  # {3}