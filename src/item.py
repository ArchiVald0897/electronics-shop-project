import csv


class InstantiateCSVError(Exception):
    pass


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        self._name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self._name}"

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
        Item.all.clear()
        try:
            with open("..\src\items.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if "name" not in row or "price" not in row or "quantity" not in row:
                        raise InstantiateCSVError("Файл item.csv поврежден")
                    name = row["name"]
                    price = float(row["price"])
                    quantity = int(row["quantity"])
                    Item(name, price, quantity)
        except FileNotFoundError:
            print("FileNotFoundError: Отсутствует файл items.csv")

    @staticmethod
    def string_to_number(num_str):
        if num_str.strip() == "":
            return 0
        return int(float(num_str))

