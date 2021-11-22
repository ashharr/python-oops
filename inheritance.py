
class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I dont know what I speak yet.")
        
class Cat(Pet):
    
    def __init__(self, name, age, color):
        super().__init__(name, age) # super is used to call parent class methods
        self.color = color
        
    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")
        
class Fish(Pet):
    pass
        
p = Pet("Tim", 19)
p.speak()
c = Cat("Bill", 34, "Brown")
c.show()
d = Dog("Tommy", 14)
d.speak()
f = Fish("Bubbles", 5)
f.speak()