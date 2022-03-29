## Ejercicio 24 ###
def imprimir (tabla):
    for i in tabla:
        print(i)
def llenarSecuencial(n):
    tabla = []
    cont = 1
    tabla = []
    for i in range(n):
        tabla.append([])
        for j in range (n):
            tabla [i]+=[cont]
            cont+=1
    return tabla 
tabla = llenarSecuencial(5)
imprimir(tabla)


  