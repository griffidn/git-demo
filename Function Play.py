from mod import *
print(Mod1.s)
Mod1.foo('test')
x = Mod1.Foo

print(x)


class Supply:
    def __init__(self, brand=None, cost=None, itemName=None):
        if brand is not None:
            self.brand = brand
        else:
            self.brand = 'No Brand'
        if cost is not None:
            self.cost = cost
        else:
            self.cost = 9999.99
        if itemName is not None:
            self.itemName = itemName
        else:
            self.itemName = 'No Name'

        self.price = self.cost * 2.5

    def calc_price(self):
        self.price = self.cost * 2.5

    def to_string(self):
        print('Item Name:', self.itemName)
        print('Brand:', self.brand)
        print('Cost:', self.cost)
        print('Price:', self.price)


class Pen(Supply):
    def __init__(self, brand=None, cost=None, color=None, itemName=None):
        super().__init__(brand, cost, itemName) # self.brand/cost initialized here
        if color is not None:
            self.color = color
        else:
            self.color = 'No Color'

    def set_color(self, color):
        self.color = color

    def to_string(self):
        super().to_string()
        print('Color:', self.color)


paper = Supply('Xerox', 5.99)
red_pen = Pen('Bic', 0.99)

paper.to_string()
red_pen.to_string()
