# Ejercicio 8
from this import s


jornada = 48
hTrabajadas = 49
pagoHora = 2
pagoExtra = 3,5
if hTrabajadas <= jornada:
    salario = hTrabajadas *pagoHora
else:
    ## Revisar
    salario= (jornada*pagoHora)+((hTrabajadas-jornada)*pagoExtra,(hTrabajadas-jornada)*pagoHora)
    print (" Su pago total es de :",salario)