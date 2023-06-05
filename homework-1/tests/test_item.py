from src.item import Item


def test_init_item():
    item = Item("Телефон", 5000, 10)
    assert item.name == "Телефон"
    assert item.price == 5000
    assert item.quantity == 10
    assert item.calculate_total_price() == 50000


def test_change_pay_rate():
    Item.pay_rate = 0.8
    assert Item.pay_rate == 0.8


def test_apply_discount():
    item = Item("Телефон", 5000, 10)
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 4000
    assert item.calculate_total_price() == 40000


def test_add_to_all():
    item = Item("Телефон", 5000, 10)
    assert item in Item.all
