from math import pow, pi
def calcula_volume(raio):
    return (4 / 3) * pi * pow(raio, 3)

raio = float(input('Insira o raio da esfera: '))

print(f'O volume da esfera é {calcula_volume(raio):.3f} m³')

