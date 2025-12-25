# another example of private attributes in python
# Private is a conceptual in python as it is not similar to other languages
# If we want to make both the attribute and variables private then we add 2 underscores in front of 
# both the variable and the method name

class Person:
    __name = "anonymous"

    # creating a private method
    def __hello(self, name):
        self.__name = name
        print(f"hello person! {name}")

    # creating a function that takes a uses a private method
    def welcome(self, name):
        self.__name = name
        self.__hello(name)

p1 = Person()

#print(p1.__name) # gives error since this is private, uncomment to see

#p1.__hello() # this will also give an error, uncomment to see

"""The reason we use private methods even though they error out when we call them outside the class is
due to the fact that these are made for other functions inside the class and are meant to be used inside that class"""

# example of how above explanation works
p1.welcome("Gaurav")