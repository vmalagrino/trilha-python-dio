# Python trabalha com escopo local e global, dentro do bloco da função o escopo é local.
# Portanto alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar a execução.
# Para usar objetos globais utilizamos a palavra reservada global, que informa ao interpretador que a var que está sendo manipulada no escopo local é global.
# Essa não é uma boa prática e deve ser evitada

# var global na raiz do programa
salario = 2000


def salario_bonus(bonus):
    # ao usar salario dentro da função, o interpretador entende que é uma var local
    global salario
    salario += bonus
    return salario


print(salario_bonus(500))  # 2500
