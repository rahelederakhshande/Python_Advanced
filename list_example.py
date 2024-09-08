class MyList(list):
    def __init__(self, data=[]):
        if self.all_str(data):
            super().__init__(data)
        else:
            raise ValueError("Only String")

    @staticmethod
    def all_str(data):
        for item in data:
            if not isinstance(item, str):
                return False
        return True


    def show_data(self):
        print(self)

    def append(self, value):
        if isinstance(value, str):
            super().append(value)
        else:
            raise ValueError("Only String")
        
    def insert(self, index, value):
        if isinstance(value, str):
            super().insert(index, value)
        else:
            raise ValueError("Only String")

    def extend(self, data_list):
        if all(isinstance(item, str) for item in data_list):
            super().extend(data_list)
        else:
            raise ValueError("Only String")
        
    def __setitem__(self, index, value):
        if isinstance(value, str):
            super().__setitem__(index, value)
        else:
            raise ValueError("Only string")
    
    def filter_data(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        filtered_data = []
        for item in self:
            if value in item:
                filtered_data.append(item)
        return filtered_data
    def join_all(self, seprator=""):
        result = seprator.join(self)
        return result
    
# isinstance() ====> isinstance(l1, MyList)
l1 = MyList(["1", "12", "python"])
l1.show_data()
try:
    l1.append(12)
except ValueError as e:
    print(e)
#l1.insert(0, 2000)
print(l1)
#print(dir(l1))
l1.extend(["python", "java"])
print(l1)
l1[4] = "3000" # ====> method ????
print(l1)
data = l1.filter_data("py")
print(data)
print(l1.join_all("#"))
#print(dir(l1))
