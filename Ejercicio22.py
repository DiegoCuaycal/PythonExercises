### Ejercicio 22
from random  import randint
def llenarSec (n):
    lista = []
    for i in range (1,n+1):
        lista += [i]
    return lista
def llenarAle (n):
    lista = []
    num = randint(1,n)
    lista +=[num]
    for i in range (n-1):
        while num in lista :
              num = randint(1,n)
        lista+=[num]
    return lista 


listaA = llenarSec(24)
listab = llenarAle(24)
for i in range (len(listaA)):
    print(" A la  persona : ",listaA[i], " es pareja con : ",listab[i])

print(listaA)
print(listab)



