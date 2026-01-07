# isdisjoint verifica se dois conjuntos não possuem elementos em comum

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

# conjunto_a e conjunto_b não possuem elementos em comum
resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

# conjunto_a e conjunto_c possuem o elemento 1 em comum
resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)
