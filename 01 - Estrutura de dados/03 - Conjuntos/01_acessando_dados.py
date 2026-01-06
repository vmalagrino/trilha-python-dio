# conjuntos em py não suportam indexação, fatiamento, precisamor converter para lista ou tupla para acessar elementos

numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])
