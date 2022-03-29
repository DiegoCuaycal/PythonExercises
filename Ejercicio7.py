# Ejercicio 7 

import random
from random import randint
zonaUsuarion= int(input(" ¿ En que zona dese disparar ? : "))
zonaPortaero = randint(1,6)
print (" La zona cubierta por el portero es : ",zonaPortaero)
if zonaUsuarion == zonaPortaero:
    print (" No ha sido un gol")
else:
     print(" Goooooooooooooooooooooool")

