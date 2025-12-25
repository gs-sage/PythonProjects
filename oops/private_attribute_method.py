"""Private(like) attributes and methods:
Conceptual Implementations in python.
Private attributes and methods are meant to be used only within the classs and are not accessible
from outside the class."""

class Account:
    def __init__(self, acc_no, acc_pass, acc_info):
        self.acc_no = acc_no
        self.acc_pass = acc_pass
        self.__acc_info = acc_info # example of private attribute

    # creating a function and using the private variable here and it will work since it is inside the class
    def reset_pass(self):
        print(self.__acc_info) # this works since this is inside the class and not outside


# creating an object for the account class
acc1 = Account("12345","abcdef","account information")
print(acc1.acc_pass) # this will print the password for the account cause the argument variable is not private

"""IMPORTANT"""
# In python if we want to make something private we add 2 underscores in front of the variable
"""So to make acc_no or acc_pass private under the init function we would do
self.__acc_no and self.__acc_pass"""

# calling the reset_pass function will work without issues
acc1.reset_pass()

# trying to print the private attribute will throw an error cause this is outside the function
print(acc1.__acc_info)