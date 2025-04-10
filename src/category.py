from typing import Any

from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):  # type: ignore

        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count = len(Product.products) if Product.products else 0

    def __str__(self) -> str:
        sum_quantity = 0
        for product in self.__products:
            sum_quantity += product.quantity
        return f"{self.name}, количество продуктов: {sum_quantity} шт."

    def add_product(self, product: Any) -> Any:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        # Формируем строку с информацией о каждом продукте
        product_str = ""
        for product in self.__products:
            product_str += str(product)
        return product_str

    @property
    def products_in_list(self):  # type: ignore
        return self.__products

    def middle_price(self):  # type: ignore
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
