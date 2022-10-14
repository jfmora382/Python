""" Solicitar dos números al usuario y calcular cuál es el mayor y cuál el menor, e imprimir los resultados. """


print(
    "\n\033[1m" + "Numeros Mayor o Menor\n")

num_1 = int(input("Ingrese el primero numero: "))
num_2 = int(input("Ingrese el segundo numero: "))


if num_1 > num_2:
    print(f"El numero {num_1} es mayor, y el numero {num_2} es menor")
elif num_2 > num_1:
    print(f"El numero {num_2} es mayor, y el numero {num_1} es menor")
else :
    print("Los dos numeros son iguales")