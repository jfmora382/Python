""" El número de pulsaciones que debe tener una persona por 
cada 10 segundos deejercicio aeróbico se calcula con la fórmula """

print("\n"+
    "\033[1m" + "Numero de Pulsaciones \n")

print(
    "\033[1m" +"Si su genero es Femenino poner 1 o si es Masculino es 2 \n")

Genero = int(input("Por favor ingresar su genero: "))



Edad = int(input("Por favor ingresar su edad: "))

if Genero == 1:
    Numero_pulsaciones = int((220-Edad)//10)
    print(f"\nEl numero de pulsaciones es  {Numero_pulsaciones}, su edad es {Edad} y su genero es Femenino")
elif Genero == 2:
    Numeros_pulsaciones = int((210-Edad)//10)
    print(f"\nEl numero de pulsaciones es {Numeros_pulsaciones}, su edad es {Edad} y su genero es Masculino")
else:
    print("\nEl valor que agrego en genero no corresponde a lso dos antes mencionados")