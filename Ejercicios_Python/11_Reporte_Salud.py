""" Un reporte de salud muestra una tabla diferente del 
índice de masa corporal IMC de una persona que se 
calcula con la fórmula IMC=P/T2en donde P es el peso 
en Kg. y T esla talla en metros. Lea un valor de P y 
de T, calcule el IMC y muestre su estado según la 
siguiente tabla: """



print(
    "\033[1m" + "Reporte de Salud\n")

Masa = float(input("Ingrese su masa corporal: "))
Talla = float(input("Ingrese su talla en metros: "))

Formula_IMC = int(Masa//(Talla**2))

if  Formula_IMC < 20 :
    
    print("Su estado es Desnutrido")
    
elif Formula_IMC >= 20 and Formula_IMC < 25 :
    
    print("Su estado es Normal")
    
elif Formula_IMC >= 25 and Formula_IMC < 30 :
    
    print("Su estado es Sobrepeso")
    
elif Formula_IMC >= 30 and Formula_IMC < 35 :
    
    print("Su estado es Obesidad Grado 1")
    
elif Formula_IMC >= 35 and Formula_IMC < 40 :
    
    print("Su estado es Obesidad Grado 2")
    
elif Formula_IMC > 40  :
    
    print("Su estado es Obesidad Grado 3")
    
else : 
    print("Error")
