"""  El precio que debe pagar un cliente por una  pizza  depende  del tamaño seleccionado,  
 como  se muestra a continuación:
 Tamaño    Precio
  1      $15.000
  2      $24.000
  3      $36.000

 Si  cada  ingrediente  adicional cuesta  $4.000. Escribir  un  programa  que solicite  al  empleado 
 encargado de registrarlas ventas, el tamaño de la pizza y el número de ingredientes adicionales y muestre al cliente el precio que debe pagar. """



print(
    "\n\033[1m" +"Pedido de Pizza\n")

tn_pizza = int(input(
    "Escriba el tamaño de la pizza, recuerde que el rango es de 1 a 3: "))
ingre = int(
    input("Hola!, Ahora digite el numero de ingredientes adicionales: "))

multiplicacion = 4000 * ingre
# print(multiplicacion)

if tn_pizza == 1:
    precio = 15000
    print(f"El precio a pagar es de: {precio + multiplicacion}")

elif tn_pizza == 2:
    precio = 24000
    print(f"El precio a pagar es de: {precio + multiplicacion}")

elif tn_pizza == 3:
    precio = 36000
    print(f"El precio a pagar es de: {precio + multiplicacion}")

else:
    print("Error, ponga un tamaño de pizza de acuerdo a los rangos dados anteriormente")
