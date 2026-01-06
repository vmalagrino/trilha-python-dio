# irmã da lista, tuplas são imutáveis enquanto listas são mutáveis
# Podemos criar tuplas através da classe tuple, ou colocando valores separados por vírgula de parenteses

# Tuplas podem armazenar qualquer tipo de objeto em Python, podemos ter tuplas que armazenam outras tuplas, com isso podemos criar estruturas bidimensionais (tabelas) e acessar informando os índices

# vírgulas ao final indicam que é uma tupla = boa prática em Python
frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)
