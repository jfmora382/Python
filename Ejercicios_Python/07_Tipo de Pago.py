""" Programa que permita a un usuario tomar una decisión del tipo de pago a usar.
Si la cuenta es menor a  $150000 pago  en  efectivo.  
Sino,  si  es  de  $150000 hasta  $300000 pago con  el  celular(dinero electrónico). 
Si es mayor a $300000 hasta $600000, pago con la tarjeta de débito. Caso contrario, pagoco n la tarjeta de crédito. """

print(
    "\n\033[1m" +"Tipo de Pago\n")

nombre = input("Ingrese su nombre:")
cuenta = int(input("Ingrese el valor de su cuenta: "))

if cuenta < 150000:
    print(f"Señor {nombre}, su cuenta es de: {cuenta}, puede pagar en efectivo")
elif cuenta >= 150000 and cuenta < 300000:
    print(f"Señor {nombre}, su cuenta es de: {cuenta}, puede pagar en efectivo o pago por celular")
elif cuenta >= 300000 and cuenta <= 600000:
    print(f"Señor {nombre}, su cuenta es de: {cuenta}, puede pagar en efectivo, pago por celular o tarjeta débito")
else:
    print(f"Señor {nombre}, su cuenta es de: {cuenta}, puede pagar en efectivo, pago por celular, tarjeta débito o crédito")