class Item:
    pay_rate = 1
    all = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)

    def calculate_total_price(self):
        return self.quantity*self.price*self.pay_rate

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        self.calculate_total_price()
