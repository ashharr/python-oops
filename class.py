class Dog:

    def __init__(self,name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def add_one(self, x):
        return x + 1
        
    def bark(self):
        print("bark")

d = Dog("Tim")
d2 = Dog("Bill")

d.bark()
print(d.get_name())
print("The dogs name is " + d.name)
print(d.add_one(5))
print(type(d))