correctos = int(input(" Ingrese el numero de aciertos : "))
errores = int(input(" Ingrese el numero de errores : "))
total = correctos + errores
pCorrecto =  (100/total)*correctos
pErores = (100/total)*errores
print(" Su puntaje final fue : "+str(correctos)+"/"+str(total))
print(" Su porcentaje de acierto es : %.2f "%(pCorrecto,pErores))