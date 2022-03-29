#### Ejercicio 18
from random import randint

v = True
aciertos =0


while v :
    op = randint(1,2)
    num1 = randint(1,10)
    num2= randint(1,10)
    if op == 1:
        res = num1*num2
        print(num1, "*",num2,"=")
        reUsuario = int(input(" Ingrese su respuesta : "))
        if reUsuario == res:
            print(" Correcto")
            aciertos+=1
        else:
            print(" Incorrecto")
            v = False
    elif op == 2:
        res = num1 // num2
        print(num1,"/",num2,"=")
        reUsuario = int(input(" Ingrese su respuesta"))
        if reUsuario == res:
            print(" Correcto")
            aciertos+=1
        else:
            print(" Incorreecto, la respuesta era : ",res)
            v = False


print(" Sus respuesta correctas ",aciertos,"")



