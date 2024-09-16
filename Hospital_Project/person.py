from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, id_):
        self.id_ = id_
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name}, Age:{self.age}"

    def edit_profile(self, name=None, age=None):
        self.name = name or self.name
        self.age = age or self.age

    @abstractmethod
    def des_role(self):
        pass

"""if __name__ == "__main__":
    p1 = Person("p1", 19, "1234")
    print(p1)"""