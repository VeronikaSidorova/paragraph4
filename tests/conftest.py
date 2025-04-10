import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture(autouse=True)
def reset_product_list():  # type: ignore
    # Сбрасываем список продуктов перед каждым тестом
    Product.products = []


@pytest.fixture
def product_1():  # type: ignore
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def product_2():  # type: ignore
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def product_3():  # type: ignore
    return Product(name="Xiaomi Redmi Note 11", description="1024GB, Синий", price=31000.0, quantity=14)


@pytest.fixture
def new_product():  # type: ignore
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture
def category_1():  # type: ignore
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def category_2():  # type: ignore
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        products=[Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )


@pytest.fixture
def json_for_test():  # type: ignore
    return [
        {
            "name": "Смартфоны",
            "description": "Разнообразные смартфоны",
            "products": [
                {
                    "name": "Samsung Galaxy S23",
                    "description": "Лучший смартфон 2023 года",
                    "price": 999.99,
                    "quantity": 10,
                },
                {"name": "iPhone 14", "description": "Новый iPhone от Apple", "price": 1099.99, "quantity": 5},
            ],
        },
        {
            "name": "Ноутбуки",
            "description": "Мощные ноутбуки для работы и игр",
            "products": [
                {"name": "Dell XPS 13", "description": "Компактный и мощный ноутбук", "price": 1299.99, "quantity": 7}
            ],
        },
    ]


@pytest.fixture
def category_iterator(category_1):  # type: ignore
    return CategoryIterator(category_1)


@pytest.fixture
def product_smartphone_1():  # type: ignore
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def product_smartphone_2():  # type: ignore
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def product_lawngrass_1():  # type: ignore
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def product_lawngrass_2():  # type: ignore
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category_without_product(): # type: ignore
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        products=[],
    )
