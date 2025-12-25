"""OOP in Python"""
# To map with real world scenarios, we started using objects in code.
# This is called object oriented programming

"""Class & Object in Python"""
# Class is a blueprint for creating objects

# creating a class
class Student:
    name = "Gaurav"

# creating an object
s1 = Student()
print(s1.name)

"""__init__ Function"""
# All classes have a function called __init__(), which is always executed when the object is being initiated. 
# These types of functions are also referred to as constructors
# Constructor always takes a special parameter known as self. Self is the reference to the objects we create

"""
# creating class
# class Student:
#   def __init__(self, fullname):
        print(self) # will print the object pointer in memory
#       self.name = fullname
# 
# creating object
# s1 = Student("John") # when self is printed, this is the object being called since there is only one object here
# print(s1.name)
"""

# The self parameter is a reference to the current instance of the class, and is used to
# access variables that belong to the class.


"""Private(like) attributes and methods:
Conceptual Implementations in python.
Private attributes and methods are meant to be used only within the classs and are not accessible
from outside the class."""