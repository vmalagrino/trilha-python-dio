# método copy cria uma cópia da lista original, parece igual mas na teoria são duas listas diferentes com ids diferentes

lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

print(id(l2))  # id diferente de lista, o que fizermos aqui não afetará a lista original
print(id(lista))  # id diferente de l2

l2[0] = 2
print(l2)  # [2, "Python", [40, 30, 20]]
print(lista)  # [1, "Python", [40, 30, 20]]