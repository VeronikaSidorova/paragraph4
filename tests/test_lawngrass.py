import pytest


def test_lawngrass_init(product_lawngrass_1): #type: ignore
    assert product_lawngrass_1.name == "Газонная трава"
    assert product_lawngrass_1.description == "Элитная трава для газона"
    assert product_lawngrass_1.price == 500.0
    assert product_lawngrass_1.quantity == 20
    assert product_lawngrass_1.country == "Россия"
    assert product_lawngrass_1.germination_period == "7 дней"
    assert product_lawngrass_1.color == "Зеленый"


def test_lawngrass_add(product_lawngrass_1, product_lawngrass_2): #type: ignore
    assert product_lawngrass_1 + product_lawngrass_2 == 16750.0


def test_lawngrass_add_error(product_lawngrass_1, product_smartphone_1): #type: ignore
    with pytest.raises(TypeError):
        res = product_lawngrass_1 + product_smartphone_1
