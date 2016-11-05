a = int(input())

def compara(lista, i):
    dic = {
        "PAPEL": {"TESOURA": "JOGADOR2","PEDRA": "JOGADOR1", "PAPEL": "EMPATE"},
        "TESOURA": {"PEDRA": "JOGADOR2","PAPEL": "JOGADOR1", "TESOURA": "EMPATE"},
        "PEDRA": {"PAPEL": "JOGADOR2","TESOURA": "JOGADOR1", "PEDRA": "EMPATE"}
        }
    return res(dic[lista[0]][lista[1]], i+1)

def res(jogador, i):
   print("CASO #{}: {}".format(i, jogador))
   
for i in range(a):
    jogada = input()
    lista = jogada.upper().split()    
    compara(lista, i)
    
