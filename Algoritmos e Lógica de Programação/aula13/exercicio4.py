def calcula_segundos(h, m, s):
    return ((h * 3600) + (m * 60) + (s))

h = int(input('Insira as horas: '))
m = int(input('Insira os minutos: '))
s = int(input('Insira os segundos: '))

print(f'O total de segundos é {calcula_segundos(h, m, s)} segundos')