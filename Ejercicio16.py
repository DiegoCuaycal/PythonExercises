## Ejercicio 16
## Juego de piedra pael o tijera
from random import randint
ganadas = 0
while ganadas <3:
    opUsuario = int(input (" Ingrese una opcion : \n1.- piedra \n2.- papael\n3.-tijera : "))
    opMaquina = randint(1,3)
    print(" La maquina eligio : ",opMaquina)
    if (opUsuario== 1 and opMaquina == 3 ) or (opUsuario == 2 and opMaquina==1) or (opUsuario == 3 and opMaquina==1):
       print (" Gana el usuario")
       ganadas +=1
    elif opUsuario == opMaquina:
        print(" Es un Empate")
    elif  opUsuario == opMaquina:
        print (" Gana la maquina")
    else:
        print(" Gana la maquina")
    print(" Ganadas ",ganadas,"\n")






