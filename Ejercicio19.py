## Ejercicio 19 ##
lista = [1, " Hola",3.5,False]
while len( lista )>0:
    print (lista)
    elem = int (input(" Ingrese la posicion dele elemento a eliminar : "))
    if elem >len (lista)-1:
       print (" El elemento esta fuara del rango \n")
       continue
    del(lista [elem])
