numero = input("Número do RA: ")

soma = 0
multiplicacao = 1

for i in numero:
    soma += int(i)
    multiplicacao *= int(i)

print(f"Multiplicação = {multiplicacao}\nSoma = {soma}")
