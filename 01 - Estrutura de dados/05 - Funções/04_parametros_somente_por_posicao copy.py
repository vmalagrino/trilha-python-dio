# Ppodemos definir parâmetros que podem ser passados posição e nomeados

# / = indica que os parâmetros antes da barra são obrigados a ser passados por posição e após a barra podem ser passados por posição ou nome, não tem mais obrigatoriedade
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
