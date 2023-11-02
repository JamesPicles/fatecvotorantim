lista1 = []
lista2 = []

for i in range(1, 6):
    lista1.append(int(input(f'Entre com o {i} valor da primeira lista: ')))

for i in range(1, 6):
    lista2.append(int(input(f'Entre com o {i} valor da segunda lista: ')))

conjunto_uniao = set(lista1).union(set(lista2))

print("Conjunto união entre as duas listas: ", conjunto_uniao)
