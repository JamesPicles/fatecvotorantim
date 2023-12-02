def totalAnimais(totalCabecas, totalPes):
    dicCoelhosePatos = {}
    totalCoelhos = ((2 * totalCabecas) - totalPes) / 2
    totalPatos = totalCabecas - totalCoelhos

    dicCoelhosePatos['numeroCoelhos'] = totalCoelhos
    dicCoelhosePatos['numeroPatos'] = totalPatos

    return dicCoelhosePatos

totalC = int(input('Digite o total de cabeças: '))
totalP = int(input('Digite o total de pés: '))
dicAnimais = totalAnimais(totalC, totalP)
numeroCoelhos = dicAnimais['numeroCoelhos']
numeroPatos = dicAnimais['numeroPatos']

print(f'{numeroPatos} patos e {numeroCoelhos} coelhos')