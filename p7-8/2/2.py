class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'
    
class ShoppingCart:
    def __init__(self, items=[]):
        self.items: list = items

    def add(self, item):
        self.items.append(item)
    
    def remove(self, name):
        self.items = [item for item in self.items if item.name != name]

    def total(self):
        return sum(item.price for item in self.items)
    
    def __str__(self):
        return '\n'.join(str(i) for i in self.items)
    