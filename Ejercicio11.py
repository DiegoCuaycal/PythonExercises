## Ejercicio 11
anioInicial = 1500
anioFinal = 2022  
r = " Los anios bisiestos entre "+anioInicial+"y"+anioFinal+"son : "
for i in range(anioInicial, anioFinal):
    if (i % 4 == 0 and  i % 100!=0)or i % 400 ==0:
        r = r +str(i)+ ", "
print(r)
