# Class Method
"""A class method is bound to the class and receives the class as an implicit first argument.
Note - static method can't access or modify class state and generally used for utility.

# Syntax
class Student:
    @classmethod
    def college(cls):
        pass"""

class Person:
    name = "anonymous"

    def change_name(self, name):
        self.name = name # from this only the name changes for the object level and class level stays what it was previously

    # one way to change the class attribute variable
    def change_class_name(self, name):
        Person.name = name # here the class attribute name gets changed 

    # second way to change class attribute variable value
    def change_class_name_v2(self, name):
        self.__class__.name = name #accessing the class to change the attribute value

    # third method using the classmethod decorator
    @classmethod
    def change_name_class(cls, name):
        cls.name = name


p1 = Person()
p1.change_name("Sam") # when we give a name here, a new attribute is created for the object and not the class
print(p1.name) # this will print the name for the object
print(Person.name) # this prints the name for the class

p1.change_class_name("John")
print(Person.name) # will print new name for class attribute

p1.change_class_name_v2("Greg")
print(Person.name)

p1.change_name_class("Joe Willis")
print(Person.name)