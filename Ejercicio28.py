## Ejercicio 28
diccionario = {}
print(type(diccionario))
indice = " nombre "
valor = " Anahi"

diccionario[indice]=valor
# diccionario.setdefault(indice,valor)
print(diccionario)

menu = True
while menu:
    op = int(input(" Elija una opcion\n1.-Agregar\2.-Salir\n "))
    if op == 1:
        indice = input(" Ingrese el indice : ")
        valor = input(" Ingrese el valor : ")
        diccionario[indice]=valor
        print(diccionario)
    elif op == 2:
        menu = False
    else:
        print(" Ingrese una opcion valida")