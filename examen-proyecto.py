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

H = float(input("Profundidad del pozo en metros: "))
Ld = float(input("Distancia que el caracol asciende durante el día en metros: "))
Ln = float(input("Distancia que el caracol desciende durante la noche en metros: "))

dias = 0
comienzo = 0
if Ld > Ln:
    while comienzo < H:
        comienzo = comienzo + Ld -Ln
        dias = dias + 1
    print(f"El caracol tardará {dias} días en salir del pozo.")

if Ld <= Ln:
    print("el caracol no sale")

#Matriz de NxM

n = int(input("Introduce el número de filas de la matriz: "))
m = int(input("Introduce el número de columnas de la matriz: "))
matrix=[]

for i in range(n):
    fila=[]
    for j in range (m):
        fila.append(0)
    matrix.append(fila)

num = 1

for i in range(n):
    for j in range(m):
        matrix[i][j]=num
        num= num+ 1

for i in range(n):
    if i%2 != 0:
        matrix[i]=list(reversed(matrix[i]))

for fila in matrix:
    print(fila)

