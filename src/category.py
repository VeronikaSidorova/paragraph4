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
        Category.product_count += len(Product.products) if Product.products else 0

    def add_product(self, product: Any) -> Any:
        if not isinstance(product, Product):
            raise ValueError("Только объекты класса Product могут быть добавлены.")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        # Формируем строку с информацией о каждом продукте
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in Product.products
        )
