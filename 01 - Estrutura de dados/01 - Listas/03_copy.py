#Copia lista para outro local na memória
lista = [1, "python", [40, 30, 20]]

l2 = lista.copy()

print(id(l2), id(lista))

l2[0] = 3

print(lista)
print(l2)