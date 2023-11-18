''' Definição de Funções '''

qtd = 5
def linha(qtd=20):
    for _ in range(0, qtd):
        print("-", end='')
    print()

linha()
print(qtd)
print("** Uso de Funções **")
linha(30)