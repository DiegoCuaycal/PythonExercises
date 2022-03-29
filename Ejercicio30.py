## Ejercicio 30
def imprimir(diccionario):
    for indice in diccionario:
        print(" Key : ",indice," Valor : ",diccionario[indice])

def agregarEstudiante(dic,codigo,nombre):
    diccionario[codigo]=[]
    diccionario[codigo].append(nombre)
    diccionario[codigo].append([])
def agregarNota(diccionario, codigo,nota):
    diccionario[codigo][1] = [nota]
def prom(lista):
    suma+= 0
    for item in lista :
        suma+= item
    return suma/len(lista)


diccionario = {}
imprimir(diccionario)
agregarEstudiante(diccionario,"001"," Anahi ")
agregarNota(diccionario,"001",10)
agregarNota(diccionario,"001",8)
imprimir(diccionario)
prom(diccionario[" 001"][1])