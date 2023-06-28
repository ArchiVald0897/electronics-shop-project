from src.item import Item


class MixinLanguage:
    languages = ("EN", "RU")

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"
        return self


class KeyBoard(MixinLanguage, Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name

