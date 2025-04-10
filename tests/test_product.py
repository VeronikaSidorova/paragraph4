import pytest

from src.product import Product


def test_product_init(product_1):  # type: ignore
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_product_price_update(new_product, category_1):  # type: ignore
    product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
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


def test_new_product(new_product, category_1):  # type: ignore
    new_product_exept = Product.new_product(new_product)
    assert new_product_exept.name == "Samsung Galaxy S23 Ultra"
    assert new_product_exept.description == "256GB, Серый цвет, 200MP камера"
    assert new_product_exept.price == 180000.0


def test_product_create():  # type: ignore
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product.name = "Iphone 15"
    product.description = "512GB, Gray space"
    product.price = 210000.0
    product.quantity = 8


def test_product_str(product_1):  # type: ignore
    assert str(product_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"


def test_product_add(product_1, product_2, product_3):  # type: ignore
    assert product_1 + product_2 == 2580000.0
    assert product_1 + product_3 == 1334000.0
    assert product_2 + product_3 == 2114000.0


def test_product_add_error(product_1, product_smartphone_1):  # type: ignore
    with pytest.raises(TypeError):
        result = product_1 + product_smartphone_1
