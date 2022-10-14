""" Leer el número de llantas de una compra y mostrar el valor que debe pagarse. 
El almacén las vende con  la  siguiente  política:  Si  se  compran  menos  de  5  llantas,  el  precio  unitario  es $240000. 
Si  se compran 6 o 7, el precio unitario es $221000, y si se compran más de 7 llantas, elprecio unitario es $180000. """

print(
    "\n\033[1m" +"Nuemro de Llantas\n")

llantas = int(input("¿Cuantas llantas desea llevar?: "))

if llantas <= 5 :
    print(f"Usted pidio {llantas} llantas, el precio unitario es de $240000, el precio total es: {240000 * llantas}")
elif llantas == 6 or llantas == 7:
    print(f"Usted pidio {llantas} llantas, el precio unitario es de $221000, el precio total es: {221000 * llantas}")
else:
    print(f"Usted pidio {llantas} llantas, el precio unitario es de $180000, el precio total es: {180000 * llantas}")