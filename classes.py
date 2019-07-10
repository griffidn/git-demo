class Order:
    # Initializer / Instance Attributes
    def __init__(self, order_number, lines):
        self.order_number = order_number
        self.lines = lines

    def add_one_line(self):
        self.lines = self.lines + 1


order_one = Order(123, 1)
order_two = Order(456, 1)

print(order_two.order_number)


class SpecialOrder(Order):
    def special_function(self):
        self.special_property = 'abc'


# Instantiate SpecialOrder class and view properties
order_three = SpecialOrder(789, 1)
order_three.special_property = "balloon"
print(order_three.order_number)
print(order_three.special_property)
