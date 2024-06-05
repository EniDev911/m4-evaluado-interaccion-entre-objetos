from abc import ABC, abstractclassmethod
from producto import Producto

class Tienda(ABC):
    
    @abstractclassmethod
    def agregar_producto(self):
        pass

    @abstractclassmethod
    def listar_productos(self):
        pass

    @abstractclassmethod
    def realizar_ventas(self):
        pass


class Restaurante(Tienda):

    def __init__(self, nombre, delevery):
        self.__nombre = nombre
        self.__delevery = delevery
        self.__productos = []
    def agregar_producto(self, producto: Producto):

        self.__productos.append(producto)

    def listar_productos(self):
        pass

    def realizar_ventas(self):
        pass

class Supermercado(Tienda):
    def __init__(self, nombre, delevery):
        self.__nombre = nombre
        self.__delevery = delevery
        self.__productos = []

    def agregar_producto(self, producto: Producto):

        self.__productos.append(producto)

    def listar_productos(self):
        pass

    def realizar_ventas(self):
        pass

class Farmacia(Tienda):
    def __init__(self, nombre, delevery):
        self.__nombre = nombre
        self.__productos = []
        self.__delevery = delevery

    def agregar_producto(self, producto: Producto):

        self.__productos.append(producto)

    def listar_productos(self):
        pass

    def realizar_ventas(self):
        pass