print("Factura de tu compra")
nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de productos comprados: "))
total = precio_unitario * cantidad
print(" El valor a pagar del producto", nombre_producto,"es:$",total)