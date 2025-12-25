"""del keyword
Used to delete object properties or object itself."""

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Shradha") 

del s1 # deleting the object

print(s1) # trying to print will now give an error.