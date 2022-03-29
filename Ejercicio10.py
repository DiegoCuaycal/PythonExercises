num = 20
r = " El numero "+str(num)+" es divisible para : "
for i in range (1,(num//2)+1,1):
    if num %i == 0:
        r += str(i)+", "
r += str(num)
print (r)

