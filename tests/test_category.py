import pytest

from src.product import Product


def test_category_init(category_1, category_2):  # type: ignore
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_1.products_in_list) == 3

    assert category_2.name == "Телевизоры"
    assert (
        category_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(category_2.products_in_list) == 1

    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 4
    assert category_2.product_count == 4


def test_add_product(category_1, new_product):  # type: ignore
    category_1.add_product((Product.new_product(new_product)))
    assert len(category_1.products_in_list) == 4


def test_category_products_property(category_1):  # type: ignore
    assert category_1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_category_str(category_1):  # type: ignore
    assert str(category_1) == "Смартфоны, количество продуктов: 27 шт."


def test_category_iterator(category_iterator):  # type: ignore
    iter(category_iterator)
    assert category_iterator.index == 0
    assert next(category_iterator) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    assert next(category_iterator) == "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    assert next(category_iterator) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"

    with pytest.raises(StopIteration):
        next(category_iterator)


def test_middle_price(category_1, category_without_product):  # type: ignore
    assert category_1.middle_price() == 140333.33
    assert category_without_product.middle_price() == 0
