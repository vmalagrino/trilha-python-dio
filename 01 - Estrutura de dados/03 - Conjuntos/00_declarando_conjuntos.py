# estrutura de dados conjunto (set) em Python
# coleçao não ordenada de elementos únicos = set não garante a ordem
# set elimina valores duplicados em um objeto iterável

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}



# podemos declarar conjuntos com chaves {} ao invés de set()
# as duas formas são válidas
linguagems = {"python", "java", "csharp", "java", "python"}
print(linguagems)  # {"python", "js", "csharp",