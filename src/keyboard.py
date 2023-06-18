from src.item import Item


class MixinLanguage:
    language = "EN"

    def __init__(self, language: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = language

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"
        return self


class KeyBoard(Item, MixinLanguage):
    pass
