altura = 5
espacios = altura
carac = 1
for i in range (altura):
    for j in range(espacios):
        print(" ",end="")
        
    for k in range(carac):
        print("* ", end="")
    espacios-=1
    carac+=1
    print()

