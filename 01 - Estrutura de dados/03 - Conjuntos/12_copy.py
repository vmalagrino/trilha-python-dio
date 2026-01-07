# copy cria uma cópia do conjunto
# visualmente são iguais, mas na teoria são dois conjuntos diferentes com ids diferentes

sorteio = {1, 23}

print(id(sorteio))  # {1, 23}

sorteio2 = sorteio.copy()

print(id(sorteio2))  # {1, 23}