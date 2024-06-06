class Producto():

	def __init__(self, nombre:str, precio:int, stock:int = 0):
		self.__nombre = nombre
		self.__precio = precio
		self.__stock = stock

	@property
	def stock(self):
		return self.__stock

	@stock.setter
	def stock(self, stock:int):

		self.__stock = 0 if stock < 0 else stock

	@property
	def nombre(self):
		return self.__nombre

	@property
	def precio(self):
		return self.__precio

	def __add__(self, other):

		if isinstance(other, Producto):
			return Producto(self.nombre, self.precio, self.stock + other.stock)
		else:
			raise TypeError("Tipo inválido para operar +")

	def __sub__(self, other):

		if isinstance(other, Producto):
			return Producto(self.nombre, self.precio, self.stock - other.stock)
		else:
			raise TypeError("Tipo inválido para operar -")

	def __eq__(self, other) -> bool:
		return self.__nombre == other.__nombre


	def __lt__(self, other):
		return self.stock < other.stock


if __name__ == "__main__":

	p1 = Producto('apple', 300, 10)
	p2 = Producto('apple', 400, 10)

	# resultado = p1 + p2
	# resultado.stock = 3
	p1 = p1 + p2
	print(p1.stock)