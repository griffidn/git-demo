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

        self.price = 9999.99
        self.calc_price()

    def calc_price(self):
        if self.cost * 2.5 <= 0:
            print(f'{self.itemName} Error: Price cannot be zero')
            print('Price is still', self.price, '\n')
        else:
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


pen1 = Pen(brand='Testbrand', cost=199.99, color='Blue', itemName='Pen1')
pen2 = Pen('Testbrand2', 299.99, 'Red', 'Pen2')
pen3 = Pen()
pen4 = Pen(itemName='Pen4', cost=0)

supply1 = Supply('testBrand3', 0.01, itemName='Supply1')

classList = [pen1, pen2, pen3, pen4, supply1]

for item in classList:
    item.to_string()
    print('')
