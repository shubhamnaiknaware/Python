class Product:
    def __init__(self, price):
        self.price = price
# read price with property
    @property
    def price(self):
        return self.__price
# change price with property els cant set attribute
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cannot be zero or less than zero ")
        self.__price = value


pen = Product(19)
print(pen.price)
# setter is needed to change value
pen.price = 10
print(pen.price)
