
## Ejercicio 15 ##

def vasos (n,x):
    total = 0
    while n>=x:
       reciclados = n//x
       sobran = n%x
       total+=reciclados
       n = reciclados + sobran
       print("N : ",n, " Reciclados : ",reciclados," Sobran",sobran," Total reciclados : ",total)
    return total

n = 60
x = 4
print(vasos(n,x))