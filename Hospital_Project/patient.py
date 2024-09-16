from person import *
class Patient(Person):
    last_id = 1000
    def __init__(self, name, age, history):
        id_ = "P" + str(Patient.last_id)
        super().__init__(name, age, id_)
        self.__history = history # Private
        Patient.last_id += 1

    @property
    def history(self):
        return self.__history
    
    @history.setter
    def history(self, new_histroy):
        if new_histroy != None and isinstance(new_histroy, str):
            self.__history = new_histroy
        else:
            raise ValueError("Invalid!")
        
    def edit_profile(self, name=None, age=None, history=None):
        super().edit_profile(name, age)
        self.__history = history or self.__history

    def des_role(self):
        print(f"{self.name} is a patient!")

if __name__ == "__main__":
    p1 = Patient("p1", 18, "history")
    print(p1)
    p1.history = "h2"
    print(p1.id_)
    p2 = Patient("p1", 18, "history")
    print(p2.id_)
    p1.edit_profile(name="P4", age=40, history="h7")
    print(p1)
    print(p1.history)
    p1.des_role()