dia = int(input('Digite o número do dia da semana: '))

match dia:
    case 1:
        nome = "Domingo"
    case 2:
        nome = "Segunda-feira"
    case 3:
        nome = "Terça-feira"
    case 4:
        nome = "Quarta-feira"
    case 5:
        nome = "Quinta-feira"
    case 6:
        nome = "Sexta-feira"
    case 7:
        nome = "Sábado"
    case _:
        nome = f"Valor {dia} inválido"
print(nome)