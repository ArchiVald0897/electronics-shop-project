import pytest
from src.phone import Phone


@pytest.fixture()
def phone():
    return Phone("iPhone 4s", 10000, 1, 7)


def test_phone__init__(phone):
    assert phone.name == "iPhone 4s"
    assert phone.price == 10000
    assert phone.quantity == 1
    assert phone.number_of_sim == 7


def test_phone_number_of_sim_setter(phone):
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3


def test_phone_number_of_sim_setter_invalid(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = -1


def test_phone_number_of_sim_setter_invalid_zero(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = 0


def test_phone__str__(phone):
    assert str(phone) == "iPhone 4s"


def test_phone__repr__(phone):
    assert repr(phone) == "Phone('iPhone 4s', 10000, 1, 7)"
