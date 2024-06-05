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
        stock = 0 if stock < 0 else stock
        self.__stock = stock

    @property
    def nombre(self):
        return self.__nombre


    def __add__(self):
        pass


if __name__ == "__main__":
    
    print(str(Producto.__name__))
    p = Producto('apple', 300)
    p.stock = 10
    print(p.stock)