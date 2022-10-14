""" Solicitar tres números al usuario e imprimirlos en orden descendente (de mayor a menor). """



print(
    "\n\033[1m" +"Orden Descendente\n")

num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))
num_3 = int(input("Ingrese el tercer numero: "))

if num_1 > num_2 and num_1 > num_3 and num_2 > num_3:
    print(f"El numero mayor es: {num_1}, el segundo es: {num_2} y el menor es: {num_3}")

elif num_2 > num_1 and num_2 > num_3 and num_1 > num_3:
    print(f"El numero mayor es: {num_2}, el segundo es: {num_1} y el menor es: {num_3}")

elif num_3 > num_1 and num_3 > num_2 and num_1 > num_2:
    print(f"El numero mayor es: {num_3}, el segundo es: {num_1} y el menor es: {num_2}")

elif num_3 > num_1 and num_3 > num_2 and num_2 > num_1:
    print(f"El numero mayor es: {num_3}, el segundo es: {num_2} y el menor es: {num_1}")