# chaves e valores nomeados

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
# vantagem: manter o valor correto independente da ordem dos argumentos, porém se mudar o nome do argumento, precisa mudar aqui também
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
# dicionário com argumentos nomeados de chave/valor, seria o melhor caso para muitos argumentos
# ** = passando um dicionário para essa função
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
