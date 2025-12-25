# Inheritance
"""When one class(child/derived) derives the properties and methods of another class(parent/base)"""

class Car:
    color = "Black" 

    def start(self):
        print("Car started..")

    @staticmethod
    def stop(): # created this static for remembering that we can create functions without the self attribute as well
        print("Car stopped...")

# creating another class inheriting the Car class
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

car1 = ToyotaCar("Venza")
print(car1.brand)

# here the ToyotaCar class object can use the Car class functions and variables
car1.start() 
car1.stop()
print(car1.color)


"""Types of Inheritance
1. Single Inheritance
2. Multi-level Inheritance
3. Multiple Inheritance"""

# Single Inheritance
"""This is what we did above with the Car and ToyotaCar class where ToyotaCar class inherited the Car class."""

# Multi-level Inheritance
"""We can continue the above pattern and create another class that inherits the ToyotaCar class.
This is an example of single inheritance since now this new class will have properties of both the Car and ToyotaCar class."""

class Venza(ToyotaCar):
    def __init__(self, type):
        self.type = type

car2 = Venza("Hybrid")
car2.start() # function from Car class
car2.stop()
print(car2.type) # from Venza class
print(car2.brand) # this gives an error since the brand is in the initializer of the ToyotaCar class and is not a separate function or variable.