a = int(input())

def res(texto, meio):
    print("{}{}".format(texto[meio:], texto[:meio]))
   
for i in range(a):
    texto = input()
    meio = int(len(texto)/2)
    res(texto[::-1], meio)
    
