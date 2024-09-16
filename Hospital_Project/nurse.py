from person import *

class Nurse(Person):
    last_id = 1000 # class attr
    def __init__(self, name, age, department):
        id1 = "N"+str(Nurse.last_id)
        super().__init__(name, age, id1)
        self.department = department
        Nurse.last_id += 1
    
    def __str__(self):
        return f"{super().__str__()}, Department: {self.department}"
    
    def edit_profile(self, name=None, age=None, department=None):
        super().edit_profile(name, age)
        self.department = department or self.department

    def des_role(self):
        print(f"{self.name} is a nurse!")

if __name__ == "__main__":
    n1 = Nurse("n1", 19, "d1")
    print(n1)
