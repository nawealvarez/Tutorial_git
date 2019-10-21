import random

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
        a= 1
    for i in numeros:
        print("El número ", a, " añadido: ", i, "\n")
        a += 1

def factorial(num):
    resultad = 1
    while num > 0:
        resultado *= num
        num -= 1
    return resultad

def factorial_recursivo(num):
    if num > 1:
        return num * factorial_recursivo((num-1))
    else:
        return 1

def fact_ternario(num):
    return num *fact_ternario(num-1) if num >1 else 1

opcion=int(input("Elija 1 para numeros primos o 2 para factorial de un numero: "))
if opcion == 1:
    numeros_primos()
    
if opcion == 2:
    numero = int(input("Ingrese un numero para hacer el factorial: "))
    cualq = random.randint(1, 3)
    if cualq == 1:
        print("El factorial de ", numero, " es: ", factorial(numero))
    elif cualq == 2:
        print("El factorial de ", numero, " es: ", factorial_recursivo(numero)) 
    elif cualq == 3:
        print("El factorial de ", numero, " es: ", fact_ternario(numero))   