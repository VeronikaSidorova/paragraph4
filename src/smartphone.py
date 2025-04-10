from src.product import Product


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):  # type: ignore
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):  # type: ignore
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
