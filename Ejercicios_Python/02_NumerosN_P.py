"""  Solicitar número al usuario y determinar si es negativo, positivo o cero. """

print(
    "\n\033[1m" + "Numero Negativo , Positivo o Cero\n")

num = int(input("Ingrese un numero: "))

if num == 0:
    print("Su numero es 0")
elif num > 0:
    print("Su numero es positivo")
else:
    print("Su numero es negativo")