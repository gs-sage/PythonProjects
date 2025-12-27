"""Polymorphism
When the same operator is allowed to have different meaning according to the context.
Good example in python for polymorphism is the operator overloading"""

print(1+2) # prints 3
print("Name" + " your college") # concatenates two strings
print([1,2,3] + [4,5,6]) # merges list

"""The above examples are called implicit overloading since the classes for them have
already been defined in python."""

print()
print("Creating a class to add complex numbers")

"""Dunder functions are functions with double underscores"""

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def show_number(self):
        print(f"{self.real}i + {self.imaginary}j")

    def add(self, second_object): # self is the object itself and we add another object as variable to add their values
        new_real = self.real + second_object.real
        new_imaginary = self.imaginary + second_object.imaginary
        return Complex(new_real, new_imaginary)
    
    # creating an add function with dunder logic
    def __add__(self, second_object): # self is the object itself and we add another object as variable to add their values
        new_real = self.real + second_object.real
        new_imaginary = self.imaginary + second_object.imaginary
        return Complex(new_real, new_imaginary)

    def __sub__(self, second_object): # self is the object itself and we add another object as variable to subtract their values
        new_real = self.real - second_object.real
        new_imaginary = self.imaginary - second_object.imaginary
        return Complex(new_real, new_imaginary)

num1 = Complex(1,3)
num1.show_number()

num2 = Complex(4,5)
num2.show_number()

add_complex = num1.add(num2) # here num1  is self since that is the object calling the add complex number function and we provide num2 as the second object
add_complex.show_number()

# after defining a dunder function I can just use the add symbol and add 2 complex numbers

num3 = num1 + num2
num3.show_number() # this will show the same output as above
