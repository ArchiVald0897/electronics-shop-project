from src.keyboard import KeyBoard


def test_keyboard_lang():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # ������� RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"
