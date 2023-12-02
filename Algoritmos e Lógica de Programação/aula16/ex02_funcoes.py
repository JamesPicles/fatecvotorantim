def primo(numero):
    i = 1
    contador = 0
    while i <= numero:
        if (numero % i) == 0:
            contador += 1
        i += 1

    if contador == 2:
        return True
    else:
        return False


def listar_primos(qtd_primos):
    lista_primos = []
    contador, i = 0, 0
    while contador < qtd_primos:
        if primo(i):
            lista_primos.append(i)
            contador += 1
        i += 1
    return lista_primos


