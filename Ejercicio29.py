

def imprimir(diccionario):
    for indice in diccionario:
        print(" Producto : ",indice," Valor : ",diccionario[indice])

diccionario = {}
diccionario["Pan"]=1.2
total = 0
menu = True
while menu :
    op = int(input(" Elija una opcion\n1.-Agregar\n2.Facturara\n3.-Salir\n "))
    if op == 1:
        indice = input(" Ingrese el indice : ")
        valor = float(input(" Ingrese el valor : "))
        diccionario[indice]=valor
        print(diccionario)
    elif op == 2:
        factura =True
        
        imprimir(diccionario)
        factura = True
        while factura:
            imprimir(diccionario)
            print(" Elija una opcion\n1.-Agregar a Factura\n2-.- Finalizar ")
            opf = int(input())
            if opf== 1:
                indice = input(" Ingrese el producto : ")
                cantidad = int (input(" Ingrese canridad : "))
                if diccionario.get(indice )is None:
                    print(" Producto no enconytrado")
                else:
                    total += float(diccionario.get(indice))*cantidad
                    print(" El total es: ",total)
            else:
                factura=False
                total=0



    elif op == 3:
       menu = False
    else:
       print(" Ingrese una opcion valida")