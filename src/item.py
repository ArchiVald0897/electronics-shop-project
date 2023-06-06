from csv import DictReader


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise ValueError('Длина наименования товара превышает 10 символов.')
        self._name = value

    def calculate_total_price(self):
        return self.quantity * self.price * self.pay_rate

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        self.calculate_total_price()

    @classmethod
    def instantiate_from_csv(cls):
        with open('src/items.csv', 'r') as file:
            reader = DictReader(file)
            for row in reader:
                item = cls(row['name'], int(row['price']), int(row['quantity']))
                cls.all.append(item)

    @staticmethod
    def string_to_number(num_str):
        return int(float(num_str))
