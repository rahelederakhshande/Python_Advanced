from patient import *
from doctor import *
from nurse import *
#docto.Doctor

class Hospital:
    def __init__(self, name):
        self.name = name
        self.entities = {
            "doctors" : {},
            "nurses" : {},
            "patients" : {}
        }
    
    def add_data(self, obj):
        type_ = type(obj).__name__.lower() + "s"
        self.entities[type_][obj.id_] = obj

    @staticmethod
    def show_info(data):
        for v in data.values(): # v ===> obj
            print(v)
        if not data:
            print("Empty")

    def display(self, obj_type=None):
        if obj_type:
            obj_type += "s"
            #data = self.entities.get(obj_type, {})
            try:
                data = self.entities[obj_type]
            except:
                print("Error")
            else:
                print("\n"+"_"*10 + obj_type + "_"*10)
                self.show_info(data)
        else:
            for key, ent in self.entities.items(): # 3
                print("\n"+"_"*10 + key + "_"*10)
                self.show_info(ent)

if __name__ == "__main__":
    h1 = Hospital("hospital1")
    d1 = Doctor("d1", 29)
    d2 = Doctor("d2", 50)
    h1.add_data(d1)
    h1.add_data(d2)
    n1 = Nurse("n1", 19, "d1")
    h1.add_data(n1)
    h1.display()
    