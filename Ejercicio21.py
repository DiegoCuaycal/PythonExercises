## Ejercicio 21 
from cProfile import label


lista1 = ["a","b","c","d","e"]
lista2 = ["c","e","f","t","g"]
listaTodo = []
lsolo1 = []
lsolo2 = []
lambas = []
listaTodo = lista1+lista2
for palabra in lista2:
    if palabra in lista2:
        lambas = lambas+[palabra]
    else:
        lsolo1 = lsolo1 + [palabra]
for palabra in lista2:
    if palabra is not  lista1:
        lsolo2 = lsolo2+ [palabra]

print (lista1)
print (lista2)
print (listaTodo)
print (lsolo1)
print (lsolo2)
print (lambas)



