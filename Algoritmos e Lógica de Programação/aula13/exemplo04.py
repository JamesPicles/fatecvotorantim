''' Definição de Funções '''
def linha(qtd=20):
    for _ in range(0, qtd):
        print("-", end='')
    print()

linha()
print("** Uso de Funções **")
linha(30)