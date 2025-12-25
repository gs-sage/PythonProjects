# Inheritance
"""When one class(child/derived) derives the properties and methods of another class(parent/base)"""

class Car:    
    def start(self):
        print("Car started..")

    @staticmethod
    def stop(): # created this static for remembering that we can create functions without the self attribute as well
        print("Car stopped...")

# creating another class inheriting the Car class
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("Venza")
print(car1.name)

# here the ToyotaCar class object can use the Car class functions
car1.start() 
car1.stop()