from csv import DictReader


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        self._name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        return self.quantity + other.quantity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            print("Длина наименования товара превышает 10 символов.")
        else:
            self._name = value

    def calculate_total_price(self):
        return self.quantity * self.price

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        self.calculate_total_price()

    @classmethod
    def instantiate_from_csv(cls):
        with open("..\src\items.csv", "r") as file:
            reader = DictReader(file)
            for row in reader:
                item = cls(row["name"], int(row["price"]), int(row["quantity"]))
                cls.all.append(item)

    @staticmethod
    def string_to_number(num_str):
        return int(float(num_str))
