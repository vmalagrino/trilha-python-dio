carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

# função enumerate retorna o índice e o valor do elemento

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")