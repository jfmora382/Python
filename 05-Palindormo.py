
print(
    "\033[1m" + "Verificación de Palabra o Frase Palindroma \n")

Palindroma = (input("Ingrese su palabra o Frase: \n"))

Palindroma = Palindroma.lower();
Palindroma = Palindroma.replace(" ", "");

PalindromaV = Palindroma[::-1]

if  Palindroma == PalindromaV :
 print("Su palabra o frase es un Palindromo")

else :
 print("Su palabra o frase no es un Palindromo")
