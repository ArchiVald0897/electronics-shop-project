"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_name_property():
    item = Item("Телефон", 1000, 1)

    # Проверяем геттер
    assert item.name == "Телефон"

    # Проверяем сеттер с корректным значением
    item.name = "Смартфон"
    assert item.name == "Смартфон"

    # Проверяем сеттер с некорректным значением
    try:
        item.name = "Это очень длинное название"
    except ValueError as e:
        assert str(e) == "Длина наименования товара превышает 10 символов."


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[0].price == 100
    assert Item.all[0].quantity == 1


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5


def test_apply_discount():
    item = Item("Смартфон", 1000, 5)

    # Проверяем правильность вычислений
    assert item.apply_discount() == 5000.0

    # Проверяем, что цена изменилась
    assert item.price == 500.0
