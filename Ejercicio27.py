## 27
def imprimir (tabla):
    for fila in tabla:
        print(" [",end="")
        for columna in fila:
            print("%3s"%columna,end ="" )
        print(" ]")
def comprobarGanador(tabla, simbolo):
    win = False
    win2 = True 
    for i in range (len(tabla)):
        if tabla [i].count(simbolo)==3:
            win = True
        for j in range (len (tabla)):
            win2 = tabla[i][j] == simbolo and win2
        if win2 == True :
            break
    if win or win2:
        return True
    else:
        return False




tabla = [[" X"," X","X "],
       [" "," "," "],
       ["X ","X ","X "]]
print(comprobarGanador(tabla,"x"))
