import json
from unittest.mock import patch, mock_open

from src.utils import read_json, create_objects_from_json


def test_read_json():
    # Пример данных, которые мы хотим вернуть из нашего "файла"
    mock_data = {
        "name": "Test",
        "value": 42,
        "active": True
    }

    # Преобразуем mock_data в строку JSON
    mock_json = json.dumps(mock_data)

    # Используем mock_open для имитации открытия файла
    with patch("builtins.open", mock_open(read_data=mock_json)):
        # Патчим os.path.abspath, чтобы вернуть любой путь, так как он не важен для теста
        with patch("os.path.abspath", return_value="mocked/path/to/file.json"):
            result = read_json("mocked/path/to/file.json")

    # Проверяем, что результат соответствует ожидаемым данным
    assert result == mock_data


def test_create_objects_from_json(json_for_test):
    # Вызов функции
    categories = create_objects_from_json(json_for_test)

    # Проверка, что количество категорий соответствует ожидаемому
    assert len(categories) == 2

    # Проверка первой категории
    assert categories[0].name == "Смартфоны"
    assert categories[0].description == "Разнообразные смартфоны"

    # Проверка второй категории
    assert categories[1].name == "Ноутбуки"
    assert categories[1].description == "Мощные ноутбуки для работы и игр"
