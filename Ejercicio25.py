## Ejercicio 25 
def imprimir (tabla):
    for i in range(len(tabla)):
        print(" [",end="")
        for j in range (len(tabla)):
            print("%3s"%tabla[i][j],end ="" )
        print(" ]")
 
def llenarVacio(n):
    tabla = []
    for i in range(n):
        tabla.append([])
        for j in range (n):
            tabla[i]+=[ " "]
    return tabla

def asteriscos (tabla, simbolo):
    if len(tabla)%2==0:
        print(" La longitud debe ser impar ")
    else:
        for i in range (len(tabla)):
            for j in range(len(tabla)):
                if i == len(tabla)//2 or j == len (tabla)//2 or i == j or i+j == len(tabla)-1:
                    tabla[i][j] = simbolo

tabla = llenarVacio(5)
imprimir (tabla) 
asteriscos (tabla, "*")
imprimir(tabla)


