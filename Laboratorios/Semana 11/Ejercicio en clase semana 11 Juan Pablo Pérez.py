print("Semana 11 ejercicio 1")

N=0
while N<=0:
    N=int(input("Ingrese un numero mayor a 0"))

    if N<0:
        print("El numero ingresado debe ser mayor a 0")
        print("")
A=0
B=1
c=0
i=2
resultado=""
resultado=str(A)
if N>2:
    resultado+=str(B)
    
    while i<N:
        C=A+b
        resultado+=str(C)
        A=B
        B=C
        i=i+1
        print(resultado)
else:
    print(resultado)



print("Semana 11 ejercicio 2")


# Pedir al usuario que ingrese un número N válido
N = int(input("Ingrese un número entero positivo para N: "))
while N <= 0:
    print("El número debe ser mayor a 0.")
    N = int(input("Intente de nuevo, ingrese un número para N: "))

# Suma de la serie a
suma_a = 0
contador_a = 1
while contador_a <= N:
    suma_a = suma_a + 1 / contador_a
    contador_a = contador_a + 1
print("La suma de la serie a es: ", suma_a)

# Suma de la serie b
suma_b = 0
contador_b = 1
while contador_b <= N:
    suma_b = suma_b + 1 / (2 ** contador_b)
    contador_b = contador_b + 1
print("La suma de la serie b es: ", suma_b)

x = int(input("Ingrese un número entero para x: "))
a = int(input("Ingrese un número entero para a: "))
limite = int(input("Ingrese un número entero para el límite de la sumatoria (n): "))

#Suma de la serie c
suma_c = 0
contador_c = 0
while contador_c <= limite:
    numerador = 1  # Para calcular el factorial de n
    denominador_k = 1  # Para calcular el factorial de k
    denominador_n_k = 1  # Para calcular el factorial de n-k
    
    for i in range(1, limite + 1):
        numerador = numerador * i
    
    
    for i in range(1, contador_c + 1):
        denominador_k = denominador_k * i
    

    for i in range(1, limite - contador_c + 1):
        denominador_n_k = denominador_n_k * i
    
    coeficiente = numerador / (denominador_k * denominador_n_k)
    suma_c = suma_c + coeficiente * (x * contador_c) * (a * (limite - contador_c))
    contador_c = contador_c + 1

print("La suma de la serie c es: ", suma_c)
    
