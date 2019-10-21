def numeros_primos():
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

def factorial(num):
    resultado = 1
    while num > 0:
        resultado *= num
        num -= 1
    return resultado

def factorial_recursivo(num):
    if num > 1:
        return num * factorial_recursivo((num-1))
    else:
        return 1

def fact_ternario(num):
    return num *fact_ternario(num-1) if num >1 else 1

print(fact_ternario(5))