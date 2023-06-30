import pytest
from src.item import Item, InstantiateCSVError
import os


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_item_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_item_apply_discount(item):
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000.0


def test_item_name():
    item = Item('Smartphone', 100, 1)
    assert item.name == 'Smartphone'


def test_item_setter_valid_len():
    item = Item('Smartphone', 100, 1)
    item.name = 'PC'
    assert item.name == 'PC'


def test_item_setter_invalid_len():
    item = Item('Smartphone', 100, 1)
    item.name = 'Электрогитара'
    assert item.name == 'Smartphone'


def test_item_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.string_to_number('5.0') == 5


def test_item_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('1241231232134') == 1241231232134
    assert Item.string_to_number('6.0') == 6
    assert Item.string_to_number('4.5') == 4


def test_item__repr__():
    item = Item('Laptop Huawei d14', 13000, 13)
    assert repr(item) == "Item('Laptop Huawei d14', 13000, 13)"


def test_item__str__():
    item = Item('Laptop Huawei d14', 13000, 13)
    assert str(item) == 'Laptop Huawei d14'


def test_item__add__():
    item = Item('Laptop', 13000, 13)
    item2 = Item('Laptop Air Pro Max', 13099, 52)
    assert item + item2 == 65


def test_item_addition_invalid_type():
    item = Item("Item 1", 10, 5)
    with pytest.raises(TypeError):
        item + 10


def test_instantiate_from_csv_success():
    Item.instantiate_from_csv()
    assert Item.instantiate_from_csv('item.csv') == None


def test_instantiate_from_csv_success():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
