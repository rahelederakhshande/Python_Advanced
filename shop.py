class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.price}, {self.category}"
    
    def show_price(self):
        print(f"price: {self.price}")

    def apply_discount(self, value):
        if value < 0 or value > 100:
            raise ValueError("between 0 and 100")
        discount = self.price * (value / 100)
        self.price -= discount

class Book(Product):
    def __init__(self, name, price, category, author, pages):
        super().__init__(name, price, category)
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{super().__str__()}, {self.author}, {self.pages}"

    def show_name(self):
        print(self.name)

class Laptop(Product):
    def __init__(self, name, price, category, processor, ram):
        super().__init__(name, price, category)
        self.processor = processor
        self.ram = ram
    
    def __str__(self):
        return f"{super().__str__()}, {self.processor}, {self.ram}"
if __name__ == "__main__":
    p1 = Product("p1", 200, "c2")
    print(vars(p1))
    b1 = Book("b1", 200, "c6", "a1", 200)
    print(b1.pages)
    print(b1.author)
    print(vars(b1))
    #print(b1)
    #b1.show_name()
    #p1.show_name()