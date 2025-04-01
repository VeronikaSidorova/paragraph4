from typing import Any


class CategoryIterator:

    def __init__(self, category_obj: Any):
        self.category = category_obj
        self.index: int = 0

    def __iter__(self):  # type: ignore
        return self

    def __next__(self):  # type: ignore
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]  # Получаем текущий товар
            self.index += 1  # Переходим к следующему товару
            return str(product)
        else:
            raise StopIteration  # Если товары закончились, вызываем исключение


# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
#     iterator = CategoryIterator(category1)
#
#     for prod in iterator:
#         print(prod)
