ganancia=0
vendedor=int(input("Ingrese numero de vendedor:"))
ventas=int(input(f"Ingrese cantidad de ventas del vendedor {vendedor}:"))
for i in range(ventas) :
    nventa=int(input(f"Ingrese el valor de la venta {i+1}:"))
    ganancia+=nventa
print(f"El salario del vendedor {vendedor} es:{ganancia+ganancia*0.05+ventas*50}$")