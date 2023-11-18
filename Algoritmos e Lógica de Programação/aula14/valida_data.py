from datetime import datetime

def valida_data(data_nascimento):
    if '/' not in data_nascimento:
        print("Por favor, digite as barras entre os números (dd/mm/aaaa).")
        return False

    partes = data_nascimento.split('/')

    if len(partes) != 3:
        print("Formato inválido. Use dd/mm/aaaa.")
        return False

    if not partes[0].isdigit() or not partes[1].isdigit() or not partes[2].isdigit():
        print("Digite apenas números para dia, mês e ano.")
        return False

    dia, mes, ano = int(partes[0]), int(partes[1]), int(partes[2])

    if not (1 <= mes <= 12 and 1900 <= ano <= datetime.now().year):
        print("Data inválida. Verifique o mês e o ano.")
        return False

    dias_no_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mes == 2 and (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
        dias_no_mes[2] = 29

    if not (1 <= dia <= dias_no_mes[mes]):
        print("Data inválida. Verifique o dia.")
        return False

    hoje = datetime.now()
    idade = hoje.year - ano - ((hoje.month, hoje.day) < (mes, dia))

    if idade < 18:
        print("Você deve ter pelo menos 18 anos para se cadastrar.")
        return False

    return True


data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

while not valida_data(data_nascimento):
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

print("Data válida. Pessoa tem mais de 18 anos.")
