from math import pow, sqrt

x1 = int(input('Entre com x1: '))
y1 = int(input('Entre com y1: '))
x2 = int(input('Entre com x2: '))
y2 = int(input('Entre com y1: '))
dx = x2 - x1
dy = y2 - y1
distância = sqrt(pow(dx, 2) + pow(dy, 2))
print('A distância entre dois pontos é: ', distância)

