from tienda import Supermercado, Farmacia, Restaurante
from producto import Producto
import os, time

if __name__ == "__main__":

    clear = lambda: os.system("cls" if os.name == "nt" else "clear")

    while True:

        tienda = int(input("¿Qué tipo de tienda desea crear?\n1. Restaurante\n2. Supermercado\n3. Farmacia\n"))
    
        tipo_tienda = {
            tienda == 1: Restaurante, 
            tienda == 2: Supermercado, 
            tienda == 3: Farmacia
        }.get(True, False)

        clear()

        if not tipo_tienda:
            print("¡Opción inválida!")
            time.sleep(1)
        else:
            break
    
    nombre_tienda = input(f"Nombre para la tienda tipo {tipo_tienda.__name__}:\n> ")
    costo_delivery = int(input("\nCosto de los delevery:\n> "))
    tienda = tipo_tienda(nombre_tienda, costo_delivery)

    opcion = int(input("\n¿Desea ingresar un producto?\n1. Sí\n2. No\n"))

    while opcion == 1:
        nombre = input("Ingrese nombre del producto:\n> ")
        precio = int(input("\nIngrese cantidad del producto:\n"))
        stock = int(input("\nIngrese stock del producto:\n"))

        producto = Producto(nombre, precio, stock)

        tienda.agregar_producto(producto)

        opcion = int(input("¿Desea ingresar un producto?\n1. Sí\n2. No\n"))
