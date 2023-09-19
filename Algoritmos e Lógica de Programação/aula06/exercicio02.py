compra = float(input('Insira aqui o valor da compra: R$'))

if (compra > 5000.00):
    print('O valor com desconto é de: R$', compra * 0.70)

else:
    if (compra <= 1000.00):
        print('O valor com desconto é de: R$', compra * 0.90)

    else:
        print('O valor com desconto é de: R$', compra * 0.80)
