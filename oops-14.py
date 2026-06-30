class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):
        return self.price > other.price

o1 = Order("Pizza",375)
o2 = Order("Pasta",550)
o3 = Order("Burger",439)
o4 = Order("Soda",75)

print(o1 > o2)

