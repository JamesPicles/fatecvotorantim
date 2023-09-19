largura = float(input('Entre com a largura do aposento, em metros: '))
comprimento = float(input('Entre com o comprimento do aposento, em metros: '))
litros = float(input('Entre com o volume da lata (L) a ser usado: '))

porta = 0.80 * 2.10


if (litros == 18):
    print('A quantidade de latas de 18L a serem compradas é de: ', ((((largura * 2.80 * 2) + (comprimento * 2.80 * 2)) - porta) / 18) / 3)

else:
    if (litros == 3.6):
        print('A quantidade de galões de 3,6L a serem comprados é de: ', ((((largura * 2.80 * 2) + (comprimento * 2.80 * 2)) - porta) / 3.6) / 3)

    else:
        print('A quantidade de latas de 1L a serem compradas é de: ', ((((largura * 2.80 * 2) + (comprimento * 2.80 * 2)) - porta) / 1) / 3)



