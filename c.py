def media(lista):
    notas = [y for y in lista[1:]]
    soma = 0
    for i in notas:
        soma += i
    return soma/lista[0]

def varianca(lista, media):
    notas = [(y - media)**2 for y in lista[1:]]
    soma = 0
    for i in notas:
        soma += i
    return soma/lista[0]

def acima_media(lista, media):
    acima = 0
    for i in lista:
        if i > media:
            acima += 1
    return acima/lista[0] * 100

while True:
    i = int(input())
    if i == 0:
        break
    for x in range(i):
        linha = input()
        lista = linha.split()
        lista = [int(y) for y in lista]
        media = media(lista)
        print("CASO #{}:".format(x+1))
        print("{:0.2f}% {:0.2f}".format(acima_media(lista, media),varianca(lista, media)))
        print()
