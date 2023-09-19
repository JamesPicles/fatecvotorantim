numero = int(input('entre com o número desejado: '))

if (numero % 3) == 0 and (numero % 5) == 0:
    print(f'O número {numero} é divisível por 3 e 5 ao mesmo tempo')

else:
    print(f'O número {numero} não é divisível por 3 e 5 ao mesmo tempo!')
