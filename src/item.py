from csv import DictReader


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

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
        return self.quantity * self.price * self.pay_rate

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        self.calculate_total_price()

    @classmethod
    def instantiate_from_csv(cls):
        with open("D:\Python\homework\exercise_13\electronics-shop-project\src\items.csv", "r") as file:
            reader = DictReader(file)
            for row in reader:
                item = cls(row["name"], int(row["price"]), int(row["quantity"]))
                cls.all.append(item)

    @staticmethod
    def string_to_number(num_str):
        return int(float(num_str))
