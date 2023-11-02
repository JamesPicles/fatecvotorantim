d = {}
lista = []
qtd = 5

for _ in range(qtd):
    nome = input('Digite o seu sobrenome: ')
    idade = int(input('Digite a sua idade: '))
    d[nome] = idade

media_idades = sum(d.values())/len(d)

for nome, idade in d.items():
    if idade >= media_idades:
        lista.append(nome)

print(f'Os sobrenomes com idades maiores que a média são: {lista}')
