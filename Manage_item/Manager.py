from Item import *
class InventoryManager:
    def __init__(self):
        self.items = {}
    def create_item(self, id_i, name, numbers, price):
        new_item = Item(id_i, name, numbers, price)
        return new_item
    
    def add_item(self, item):
        if item.id_i not in self.items:
            self.items[item.id_i] = item
            print("added!")
        else:
            print("Exists!")
    
    def remove_item(self, id_i):
        if id_i in self.items:
            del self.items[id_i]
            print("removed!")
        else:
            print("not found!")
    
    def display_item(self):
        for item in self.items.values():
            print(item)

    def edit_item(self, id_i):
        if id_i in self.items:
            new_name = input("new name: ")
            new_price = input("new price: ")
            new_number = input("new numbers: ")
            # 'asd' ===> True, '' ===> False
            self.items[id_i].name = new_name or self.items[id_i].name
            self.items[id_i].price = int(new_price or self.items[id_i].price)
            self.items[id_i].numbers = int(new_number or self.items[id_i].numbers)
            print("Edited!")
        else:
            print("not found!")

    def search(self, name):
        for item in self.items.values():
            if item.name == name:
                print(item)
    def details(self):
        num = len(self.items)
        print(f"Numbers of poducts: {num}")
        """total_price = []
        for item in self.items.values():
            total_price.append(item.price)
        print(total_price)
        sum_prices = sum(total_price)"""
        total_price = [item.price for item in self.items.values()]
        sum_prices = sum(total_price)
        print(f"Prices: {sum_prices}")

m1 = InventoryManager() # {}
#print(m1.items)
item1 = m1.create_item("1", "B", 3, 200) # Item
item2 = m1.create_item("2", "B", 3, 200) # Item
m1.add_item(item1)
m1.add_item(item2)
#m1.display_item()
#m1.edit_item("1")
#m1.display_item()
m1.search("B")
m1.details()
"""print(m1.items)
m1.remove_item("1")
print(m1.items)"""