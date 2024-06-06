from tienda import Supermercado, Farmacia, Restaurante
from producto import Producto
import os, time

if __name__ == "__main__":

    clear = lambda: os.system("cls" if os.name == "nt" else "clear")

    while True:
        opciones = ["1. Restaurante", "2. Supermercado", "3. Farmacia"]
        print("¿Qué tipo de tienda desea crear?", opciones, sep="\n")
        tienda = int(input("> "))
    
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

        clear()
        nombre = input("Ingrese nombre del producto:\n> ")
        precio = int(input("\nIngrese el precio del producto:\n> "))
        stock = int(input("\nIngrese stock del producto:\n> "))

        tienda.agregar_producto(nombre, precio, stock)

        opcion = int(input("\n¿Desea ingresar otro producto?\n1. Sí\n2. No\n"))
    while True:

        clear()

        opciones = ["1. Listar productos existentes", "2. Realizar una venta", "3. Salir del programa"]
        print("¿Qué operación desea realizar?", *opciones, sep="\n")
        operacion = int(input("> "))
        if operacion == 1:
            print(*tienda.listar_productos(), sep="\n\n")
        elif operacion == 2:
            tienda.realizar_ventas()
        elif operacion == 3:
            break


