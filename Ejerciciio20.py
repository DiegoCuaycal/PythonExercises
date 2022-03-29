#### Ejercicio 20
lista = [" Hola "," gato","perro", " palabra", " hola"]
print(lista)
for i in range ((len(lista)-1), -1,-1):
    if lista[1] in lista[:i]:
        del (lista[i])
print(lista)