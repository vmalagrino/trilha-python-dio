# difference retorna a diferença entre dois conjuntos

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# o que está em a e não está em b
resultado = conjunto_a.difference(conjunto_b)
print(resultado)

# o que está em b e não está em a
resultado = conjunto_b.difference(conjunto_a)
print(resultado)
