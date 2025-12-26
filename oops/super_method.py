# Super Method
"""super() method is used to access methods of the parent class.
In inheritance super means parent"""

class Car:
    def __init__(self, type):
        self.type = type
        print("Initializing Car class") # added for testing and learning purposes

    @staticmethod
    def start():
        print("Car started..")

    def stop(self):
        print("Car stopped...")

# to inherit the type of the parent class we can't just use a variable and assign it to self 
"""since self is the object for the current class we create. So in those cases we use super() to get the methods and initialize the
parent class inside the child class to have the attributes that are needed to be shared by all child classes"""
class Toyota(Car):
    def __init__(self, name, type):       
        super().__init__(type) # using super to call the initializer for the parent class, 
        #so this will initialize the type and also print the statement in the parent class initializer
        self.name = name
        super().start() # calling the parent method here

car1 = Toyota("Corolla","Gas") 
print(car1.name)
print(car1.type)

car2 = Car("electric")
print(car2.type)