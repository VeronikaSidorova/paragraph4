import pytest


def test_smartphone_init(product_smartphone_1): #type: ignore
    assert product_smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone_1.price == 180000.0
    assert product_smartphone_1.quantity == 5
    assert product_smartphone_1.efficiency == 95.5
    assert product_smartphone_1.model == "S23 Ultra"
    assert product_smartphone_1.memory == 256
    assert product_smartphone_1.color == "Серый"


def test_smartphone_add(product_smartphone_1, product_smartphone_2): #type: ignore
    assert product_smartphone_1 + product_smartphone_2 == 2580000.0


def test_smartphone_add_error(product_smartphone_1): #type: ignore
    with pytest.raises(TypeError):
        result = product_smartphone_1 + 1
