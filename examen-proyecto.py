#numeros random

num = input("Introduce un número mayor de 4 dígitos: ")
intentos = 3
if intentos > 0:
    while intentos > 0:
        if len(num) < 4:
            print("El número debe ser mayor de 4 dígitos.")
            num = input(f"Introduce un número mayor de 4 dígitos. Te quedan {intentos} intentos: ")
            intentos -= 1
        else:
            intentos=0
            if len(num) %2 == 0:
                num = str(int(num)**2)
                mid = int(len(num)/2)
                mid1 = mid-1
                mid2 = mid
                print(num[mid1])
                print(num[mid2])
                print(num)
            elif len(num) %2 != 0:
                num = str(int(num)**2)
                mid = int(len(num)/2)
                mid1= mid
                print(num[mid1])
                print(num)
     
elif intentos==0:
    print("Has agotado tus intentos. Vuelve a intentarlo más tarde.")

#Ejercicio del Caracol

H = float(input("Introduce la profundidad del pozo en metros: "))
Ld = float(input("Introduce la distancia que el caracol asciende durante el día en metros: "))
Ln = float(input("Introduce la distancia que el caracol desciende durante la noche en metros: "))

dias = 1
altura_actual = Ld
if Ld>Ln:
    while altura_actual < H:
        altura_actual -= Ln
        altura_actual += Ld
        dias += 1
    print(f"El caracol tardará {dias} días en salir del pozo.")

else:
    print("El caracol no sale :(")

#Matriz de NxM

n = int(input("Introduce el número de filas de la matriz: "))
m = int(input("Introduce el número de columnas de la matriz: "))

matrix = [[0]*m for i in range(n)]

num = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            matrix[i][j] = num
            num += 1
    else:
        for j in range(m-1, -1, -1):
            matrix[i][j] = num
            num += 1

for fila in matrix:
    print(fila)

