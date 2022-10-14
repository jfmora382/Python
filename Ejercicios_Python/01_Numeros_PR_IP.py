"""Par o impar. Solicitar número al usuario y determinar si es par, impar o es cero. """

print(
    "\n\033[1m" + "Numero Par , Impar o Cero\n")

num = int(input("Ingrese un numero: "))

if num == 0:
    print("Su numero es 0")
elif num % 2 == 0:
    print("Su numero es par")
else:
    print("Su numero es impar")