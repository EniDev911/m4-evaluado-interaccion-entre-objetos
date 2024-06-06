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

	def agregar_producto(self, nombre:str, precio:int, stock:int = 0):

		producto = Producto(nombre, precio, 0)
		if producto in self.__productos:
			index = self.__productos.index(producto)
			self.__productos[index] += producto
		else:
			self.__productos.append(producto)

	def listar_productos(self):
		print(*[f"Nombre: {p.nombre}\nPrecio: {p.precio}" for p in self.__productos], sep="\n\n")

	def realizar_ventas(self):
		pass

class Supermercado(Tienda):

	def __init__(self, nombre, delevery):
		self.__nombre = nombre
		self.__delevery = delevery
		self.__productos = []

	def agregar_producto(self, nombre:str, precio:int, stock:int = 0):
		producto = Producto(nombre, precio, stock)

		if producto in self.__productos:
			index = self.__productos.index(producto)
			self.__productos[index] += producto
		else:
			self.__productos.append(producto)

	def listar_productos(self) -> list:
		return [
			f"Nombre: {p.nombre}\nPrecio: ${p.precio}\nStock: {p.stock} (Pocos productos disponibles)"
			if p.stock < 10
			else f"Nombre: {p.nombre}\nPrecio: ${p.precio}\nStock: {p.stock}"
			for p in self.__productos
			]

	def realizar_ventas(self, nombre:str, cantidad:int):

		for p in self.__productos:
			if nombre == p.nombre and p.stock > 0:
				p.stock -= cantidad
	

class Farmacia(Tienda):

	def __init__(self, nombre, delevery):
		self.__nombre = nombre
		self.__delevery = delevery
		self.__productos = []

	def agregar_producto(self, nombre:str, precio:int, stock:int = 0):

		producto = Producto(nombre, precio, stock)

		if producto in self.__productos:
			index = self.__productos.index(producto)
			self.__productos[index] += producto
		else:
			self.__productos.append(producto)

	def listar_productos(self) -> list:

		return [
			f"Nombre: {p.nombre}\nPrecio: ${p.precio} (Envío gratis al solicitar este producto)"
			if p.precio > 15000
			else f"Nombre: {p.nombre}\nPrecio: ${p.precio}"
			for p in self.__productos
			]


	def realizar_ventas(self, nombre: str, cantidad: int):

		for p in self.__productos:
			if nombre == p.nombre and p.stock > cantidad and cantidad <= 3:
				producto -= cantidad


if __name__ == "__main__":
	# r1 = Restaurante('uja', 3000)
	# r1.agregar_producto('hamburguesa', 5000, 4)
	# r1.agregar_producto('papas fritas', 4000, 4)
	# r1.agregar_producto('hamburguesa', 200, 4)
	# r1.listar_productos()

	# Farmacia
	# f1 = Farmacia('cruz verde', 2000)
	# f1.agregar_producto('paracetamol', 5000, 4)
	# f1.agregar_producto('aspirina', 4000, 4)
	# f1.agregar_producto('dianol', 119000, 10)
	# print(*f1.listar_productos(), sep="\n\n")

	# Supermercado
	s1 = Supermercado('unimarc', 1000)
	s1.agregar_producto('super8', 400, 40)
	s1.agregar_producto('super8', 400, 10)
	s1.realizar_ventas('super8', 12)
	s1.agregar_producto('turron', 1000, 4)
	s1.agregar_producto('gomitas', 800, 9)

	print(*s1.listar_productos(), sep="\n\n")