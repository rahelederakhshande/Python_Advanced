from person import *

class Doctor(Person):
    last_id = 1000
    def __init__(self, name, age):
        d_id = "D" + str(Doctor.last_id)
        super().__init__(name, age, d_id)
        Doctor.last_id += 1

    def des_role(self):
        print(f"{self.name} is a doctor!")

if __name__ == "__main__":
    d1 = Doctor("d1", 43)
    print(d1)
    d1.edit_profile(age=38)
    print(d1)