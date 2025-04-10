from typing import Any

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    products: list = []

    def __init__(self, name, description, price, quantity):  # type: ignore
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

        Product.products.append(self)

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other):  # type: ignore
        if type(other) is Product:
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @property
    def price(self) -> Any:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> Any:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            confirmation = input(
                f"Вы уверены, что хотите понизить цену с {self.__price} до {new_price}? " f"Если да введите y! (y/n): "
            )
            if confirmation.lower() != "y":
                print("Цена не изменена.")
                return

        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict) -> Any:
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")

        # Проверка на существующий товар
        for existing_product in cls.products:
            if existing_product.name == name:
                # Если товар существует, обновляем количество и цену
                existing_product.quantity += quantity
                if price > existing_product.price:
                    existing_product.price = price  # Устанавливаем более высокую цену
                return existing_product

        # Если товар не существует, создаем новый
        new_product = cls(name, description, price, quantity)
        category.add_product(new_product)
        return new_product
