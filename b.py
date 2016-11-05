a = int(input())

def res(texto, meio):
    texto = texto[::-1]
    print("{}{}".format(texto[meio:], texto[:meio]))
   
for i in range(a):
    texto = input()
    meio = int(len(texto)/2)
    res(texto, meio)
    
