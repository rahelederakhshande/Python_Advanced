from patient import *
from nurse import *
from doctor import *


class Hospital:
    def __init__(self,name) :
        self.name = name
        self.entities = {
            "doctors" : {},
            "patients" : {},
            "nurses" :{}
        }

    def __str__(self) -> str:
        return f" Name: {self.name}"
    
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
    
    def remove(self,obj_id):
        for group in self.entities.values():
            if obj_id in group:
                del group[obj_id]
                return f"{obj_id} Reomved"
        return "Not Found"
    
    def search(self,**var):
        results = []
        for group in self.entities.values():
            for obj in group.values():
                flag = True
                for attr,val in var.items():
                    if getattr(obj , attr, None) != val:
                        flag = False
                        break
                if flag:
                    results.append(obj) 
        return results



    

if __name__ == "__main__":
    h1 = Hospital("Alavi")
    d1 = Doctor("ali",19)
    d2 = Doctor("Mina",28)
    n1 = Nurse("Nina",35,"d1")
    h1.add_data(d1)
    h1.add_data(d2)
    h1.add_data(n1)
    #h1.remove("D1000")
    res = h1.search(department = "d1")
    for obj in res:
        print(obj)