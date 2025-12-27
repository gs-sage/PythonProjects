"""Property Decorator
We use @property decorator or any method in the class to use the method as a property"""

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math) / 300 * 100) + "%" # assuming 100 is total for all subjects, uncomment to check the below examples

    """Comment out this part of the code to see how this specific block makes a difference"""
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 300 * 100) + "%"


stu1 = Student(98, 95, 96)
print(stu1.percentage) # here the percentage is calculated for the student

# Now if we change the value of one subject
stu1.phy = 100
print(stu1.phy) # confirming the change took place for the subject marks.

# and then print the percenctage it will still be the same
print(stu1.percentage) # this happens because we have the percentage defined while initializing the object, comment out property decorator to confirm.

"""Once we define the new function with the property decorator the values are updated instantly."""
stu1.phy = 50
print(stu1.phy)
print(stu1.percentage) # this will reflect new value, please keep in mind above example will also show correct cause we have defined a property decorator, please comment
# that out to see the difference

"""Couple of ways to fix that, we can create a separate function for percentage and call
that each time the value is changed but that is tedious and so we use the property decorator.
When we use this decorator it will always take the latest value for its arguments. Please note
the above function with the property decorator was created after testing above examples"""

