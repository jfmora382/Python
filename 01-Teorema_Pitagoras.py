

print("\t Teorema de Pitagoras\n")

# Datos

print("Escribir " + "\033[1m" + "Hipotenusa" +
      "\033[1m" + " si es la que desea encontrar\n")
print("Escribir " + "\033[1m" + "CatetoA" +
      "\033[1m" + " si es la que desea encontrar\n")
print("Escribir " + "\033[1m" + "CatetoB" +
      "\033[1m" + " si es la que desea encontrar\n")
Buscador = input("Ingrese que quiere buscar: \n")

if Buscador == "Hipotenusa":
    a = float(input("Ingrese cateto a: "))
    b = float(input("Ingrese cateto b: "))
# hipotenusa
    h = float(((a**2)+(b**2))**(1/2))
# Resultado
    print("La hipotenusa es:", h)
elif Buscador == "CatetoA":

    h = float(input("Ingrese hipotenusa: "))
    b = float(input("Ingrese cateto b: "))
# hipotenusa
    a = float(((h**2)-(b**2))**(1/2))
# Resultado
    print("El CatetoA es:", a)


elif Buscador == "CatetoB":
    h = float(input("Ingrese hipotenusa: "))
    a = float(input("Ingrese cateto a: "))
# hipotenusa
    b = float(((h**2)-(a**2))**(1/2))
    print("El CatetoB es:", b)
else:
    print("Lo que Busca no exite")



