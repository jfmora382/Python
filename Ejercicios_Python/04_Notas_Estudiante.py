""" Solicitar cinco (5)notas de 0.0 a 5.0 a un estudiante y calcular promedio.
Mostrar como "Aprobó" si el promedio es mayor o igual a 3.0, o mostrar "No aprobó" si su nota es menor a 3.0. """


print(
    "\n\033[1m" + "Notas del Estudiante\n")


print("\nIngesar sus notas desde 0.0 hasta 5.0\n")

num_1 = float(input("Ingrese su primera nota: "))
num_2 = float(input("Ingrese su segunda nota: "))
num_3 = float(input("Ingrese su tecera nota: "))
num_4 = float(input("Ingrese su cuarta nota: "))
num_5 = float(input("Ingrese su quinta nota: "))

prom = (num_1 + num_2 + num_3 + num_4 + num_5) / 5

if prom > 5.0:
    print("Por favor digite las notas dentro del rango que se le mostro antes")
elif prom >= 3.0 and prom <= 5.0:
    print("Aprobó")
else:
    print("No aprobó")