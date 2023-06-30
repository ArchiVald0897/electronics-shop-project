import pytest
from src.keyboard import Keyboard


def test_keyboard_str():
    kb = Keyboard('Dark Project', 9600, 5)
    assert str(kb) == 'Dark Project'


def test_keyboard_change_language_default():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == 'EN'


def test_keyboard_change_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    kb.change_lang()
    assert kb.language == 'RU'

    kb.change_lang()
    assert kb.language == 'EN'

    kb.change_lang()
    assert kb.language == 'RU'
