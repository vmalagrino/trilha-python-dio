# Filtrar lista
# Verifica se o valor da lista se divisivel por 2 resultando em 0 (número par), é adicionado a lista pares
numeros = [1, 30, 21, 2, 9, 65, 34]

# Versão professor
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# versão de estudo mais fácil de entender inicialmente
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números pares:", pares)
print("Números ímpares:", impares)

# Versão professor
# Modificar valores - elevar ao quadrado
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)
