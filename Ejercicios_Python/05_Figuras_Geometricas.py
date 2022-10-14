"""Crear un programa con un menú de opciones,
que permita calcular las áreas de figuras geométricas: cuadrado, rectángulo, triángulo, círculo, rombo y trapecio.
"""


print(
    "\n\033[1m" +"Area de Figuras Geometricas\n")


print("Digite el numero de la figura geométrica que deseé calcular el area \n")
print("1 = cuadrado")
print("2 = rectángulo")
print("3 = triángulo")
print("4 = círculo")
print("5 = rombo")
print("6 = trapecio\n")

num_fig = int(input("Ingrese el numero de la figura geométrica: "))

if num_fig == 1:
    print("\nArea del Cuadrado\n ")
    num_1 = float(input("Ingrese el lado del cuadrado: "))
    area = num_1 * num_1
    print(f"El area del cuadrado es: {area}")

elif num_fig == 2: 
    print("\nArea del Rectángulo\n")
    num_1 = float(input("Ingrese la base: "))
    num_2 = float(input("Ingrese la altura: "))

    area = num_1 * num_2
    print(f"El area del rectángulo es: {area}")

elif num_fig == 3:
    print("\nArea del Triángulo\n")
    num_1 = float(input("Ingrese la base: "))
    num_2 = float(input("Ingrese la altura: "))

    area = (num_1 * num_2) / 2
    print(f"El area del triángulo es: {area}")

elif num_fig == 4:
    print("\nArea del Círculo\n")
    num_1 = float(input("Ingrese el radio del circulo: "))
    area = (num_1**2) * 3.14
    print(f"El area del círculo es: {area}")

elif num_fig == 5:
    print("\nArea del Rombo\n")
    num_1 = float(input("Ingrese la diagonal Mayor: "))
    num_2 = float(input("Ingrese la diagonal Menor: "))
    area = (num_1* num_2) / 2
    print(f"El area del Rombo es: {area}")

elif num_fig == 6:
    print("\nArea del Trapecio\n")
    num_1 = float(input("Ingrese la base Mayor: "))
    num_2 = float(input("Ingrese la base Menor: "))
    num_3 = float(input("Ingrese la altura: "))

    area = ((num_1 + num_2) * num_3) / 2
    print(f"El area del trapecio es: {area}")

else:
    print("Debe elegir una opcion de las que se mostraron antes")