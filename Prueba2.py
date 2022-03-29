## Prueba
## Diego Cuaycal

numero = int(input(" Ingrese un numero : "))

for i in range (1, numero +1,1):
    if( i % 3 == 0 and i % 5 == 0 ): print ( " FizzBuz ")
    elif (i % 3 == 0): print (i, " fizz ")
    elif ( i % 5 == 0 ): print ( i, " Buzz")
      
