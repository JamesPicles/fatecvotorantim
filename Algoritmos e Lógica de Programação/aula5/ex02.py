nota1 = float(input('Entre com o valor da nota 1: '))
nota2 = float(input('Entre como o valor da nota 2: '))
nota3 = float(input('Entre como o valor da nota 3: '))

media = (nota1 + nota2 + nota3) / 3
print("Sua média é:  ", media)

if (media < 3.0):
    print(f'Você está reprovado!!!')

else:
    if (media < 7.0):
        print(f'Você ficou de exame!')
        print("Você tem que tira no mínimo: ", 12 - media)
                
    else:
        print('Aprovado')


