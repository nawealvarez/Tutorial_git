numeros = []
for i in range(1,100):
    if i == 2:
        numeros.append(i)
    elif i == 3:
        numeros.append(i)
    elif i == 5:
        numeros.append(i)
    elif (i % 2)==0:
        continue
    elif (i % 3)==0:
        continue
    elif(i % 5)==0:
        continue
    else:
        numeros.append(i)

print("Numero añadidos: \n")    
a= 1
for i in numeros:
    print("El número ", a, " añadido: ", i, "\n")
    a += 1