x = float(input('Entre com o valor de x: '))
y = float(input('Entre com o valor de y: '))
z = float(input('Entre com o valor de z: '))

if ( (x + y > z) and (x + z > y) and (y + z > x)):
    # é um triângulo
    if (x == y == z):
        print('É um triângulo equilátero')
    elif (x == y) or (x == z) or (y == z):
        print('É um triângulo isósceles')
    else:
        print('É um triânguo escaleno')

else:
    # é um triângulo
    print('Os lados não formam um triângulo')