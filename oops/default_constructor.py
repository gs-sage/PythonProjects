# Notes on constructor and default constructor

"""Default constructor are created by default in python. If we don't create it python will
create it for us.
When we initialize an object in python like s1 = Student() the paranthesis is used to call the 
constructor.
"""

"""IMPORTANT
In python if there is more than one constructor, python will take the later one and not the prior constructors.
It takes the last defined constructor in the class."""

# creating class
class Student:
    def __init__(self): # this is a default constructor
        print("This is from default constructor")

    def __init__(self, name): # this is a custom constructor or parameterized constructor
        print(self) # will print the object pointer in memory
        self.name = name
 
# creating object
s1 = Student("John") # when self is printed, this is the object being called since there is only one object here
print(s1.name)