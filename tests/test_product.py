from src.category import Category
from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5

def test_product_price_update(new_product, category_1):
    product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }

    new_product = Product.new_product(product_data)

    assert new_product.price == 180000.0

    new_product.price = 200000.0
    assert new_product.price == 200000.0

    # Проверяем, что цена не может быть установлена на отрицательное значение
    new_product.price = -100.0
    assert new_product.price == 200000.0

    # Проверяем, что цена не может быть установлена на ноль
    new_product.price = 0.0
    assert new_product.price == 200000.0


def test_new_product(new_product, category_1):
    new_product_exept = (Product.new_product(new_product))
    assert new_product_exept.name == "Samsung Galaxy S23 Ultra"
    assert new_product_exept.description == "256GB, Серый цвет, 200MP камера"
    assert new_product_exept.price == 180000.0