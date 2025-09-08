class ShoppingCart:

    def __init__(self):
        self.items = []

    def add(self,name_item,qty):
        item = (name_item,qty)
        self.items.append(item)

    def remove(self,item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                return

    def total(self):
        total = 0
        for i in self.items:
            total += i[1]
        return total

buy = ShoppingCart()

buy.add('apple',100)
buy.add('banana',50)
print(buy.total())#покупка все гуд

buy.remove('banana')
print(buy.total())#remove все гуд


