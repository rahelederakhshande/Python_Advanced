class Item:
    def __init__(self, id_i, name, numbers, price):
        self.id_i = id_i
        self.name = name
        self.numbers = numbers
        self.price = price
    def __str__(self):
        return f"ID:{self.id_i}, Name:{self.name}, Nnumbers:{self.numbers}, Price:{self.price}"
    def get_price(self):
        print(f"Price: {self.price}")
    def get_name(self):
        print(f"Name: {self.name}")

if __name__ == "__main__":
    item1 = Item(1, "A", 3, 200)
    print(item1.price)
    print(item1)
    item1.get_name()
    item1.get_price()