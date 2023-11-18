def ehprimo(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

x = int(input('Digite um número inteiro: '))

if ehprimo(x):
    print(f'O número {x} é primo!')

else:
    print(f'O número {x} não é primo!')