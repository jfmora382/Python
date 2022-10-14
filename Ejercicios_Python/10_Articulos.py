"""  Un  local  vende  sus  productos  con  la siguiente  promoción.
 Si  compra  hasta  5  artículos,  no  hay descuento. Si compra más de 5 artículos, pero menos de 10, el precio unitario se reduce en 5%. 
 Si compra 10 o más artículos, el precio unitario se reduce en 8%. Ingrese un dato de cantidad y el valor del precio unitario original. 
 Calcule y muestre el valor total apagar. """
 
 
print(
    "\n\033[1m" +"Articulos de un Local\n")

cant = int(input("Ingrese la cantidad de los productos: "))
val_unit = int(input("Ingrese el precio unitario del producto: "))
pre_tol = val_unit * cant

if cant <= 5:
    print(f"Los articulos son: {cant}, el precio unitario es: {val_unit}, el precio total de su compra es: {pre_tol}")
if cant > 5 and cant <= 10:
    descuento = 0.5
    prec_desc = int(pre_tol * descuento)

    print(f"Los articulos son: {cant}, el precio unitario es: {val_unit}, el descuento es del 5%, el precio total de su compra es: {prec_desc}")

elif cant > 10:
    descuento = 0.8
    prec_desc = int(pre_tol * descuento)
    print(f"Los articulos son: {cant}, el precio unitario es: {val_unit}, el descuento es del 8%, el precio total de su compra es: {prec_desc}")