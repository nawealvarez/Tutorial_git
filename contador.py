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

def ordenar(numeros):
    ordenada = sorted(numeros)
    return ordenada

def bubbleSort(numeros):
    comparaciones = 0
    n = len(numeros)
    for i in range(1, n):
        for j in range(n-i):
            comparaciones += 1

            if numeros[j] > numeros[j+1]:
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
    return numeros

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

nombre = input('Ingrese su nombre: ')
opcion=int(input("Elija 1 para numeros primos, 2 para factorial de un numero o 3 para ordenar una lista: "))
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

if opcion == 3:
    lista = []
    respuesta = True
    while respuesta:
        numero = int(input('Ingrese un numero a la lista: '))
        lista.append(numero)
        op = int(input('Desea añadir otro numero? 1-Si, 2-No: '))
        if op == 2:
            respuesta = False
    cualq = random.randint(1, 2)
    if cualq == 1:
        print("La lista desordenada: ", lista, " la lista ordenada: ", ordenar(lista))
    elif cualq == 2:
        print("La lista desordenada: ", lista, " la lista ordenada: ", bubbleSort(lista))

print('Gracias por usar el sistema ',nombre, ' :D')