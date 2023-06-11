"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
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


def test_name_shorter_than_10_characters():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'


def test_calculate_total_price():
    item = Item('Телефон', 10000, 5)
    assert item.calculate_total_price() == 50000


def test_apply_discount():
    item = Item('Телефон', 10000, 5)
    item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 9000
    assert item.calculate_total_price() == 45000


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_invalid_string_to_number():
    with pytest.raises(ValueError):
        Item.string_to_number('abc')


def test_magical_methods():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == "Смартфон"