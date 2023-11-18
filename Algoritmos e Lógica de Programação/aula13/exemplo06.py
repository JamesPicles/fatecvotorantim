qtd = 5
def linha(qtd=20):
    print(qtd, 'dentro')
    for _ in range(0, qtd):
        print("-", end='')
    print()

linha()
print(qtd, 'fora')
print("** Uso de Funções **")
linha(30)