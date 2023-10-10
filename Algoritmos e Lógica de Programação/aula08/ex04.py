frase = input('Digite a frase: ')
qtd = 0
for letra in frase:
    if letra.lower() in 'aeiou':
        qtd = qtd + 1

print(f'A frase possui {qtd} vogais')


