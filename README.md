# Проект paragraph4
## Описание
Проект paragraph4 -  

## Установка
Клонируйте репозиторий:
```
git clone git@github.com:VeronikaSidorova/paragraph4.git
```

## Использование
1. Созданы классы. \
Product. Свойства: название (name), описание (description), цена (price), количество в наличии (quantity).\
Category. Свойства: название (name), описание (description), список товаров категории (products).
2. Созданы классы. \
Smartphone. Свойства: название (name), описание (description), цена (price), количество в наличии (quantity), 
производительность (efficiency), модель (model), объем встроенной памяти (memory), цвет (color).\
LawnGrass. Свойства: название (name), описание (description), цена (price), количество в наличии (quantity),
страна-производитель (country), срок прорастания (germination_period), цвет (color).
3. Абстрактный класс BaseProduct является родительским для Product.
4. Класс PrintMixin распечатывает в консоль информацию о том, от какого класса и с какими параметрами был создан объект.

## Тестирование
Наш проект покрыт тестами. Для их запуска выполните команду:
```
pytest
```