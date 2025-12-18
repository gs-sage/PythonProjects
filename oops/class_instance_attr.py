"""Class and Instance Attributes
Two types of attributes:
Class attributes are common for all objects which are owned by class. For example the college name for the school
database will be same for each student enrolled there. So we define the college name just once, outside constructors
for the whole class to access. 

Instance attributes are different based on what the objects require. For example in the Student class,
each object we create for it can have different name for the student. In this case, name is a instance attribute and
these are noted by self.name, self.marks cause self is a reference for objects."""

class Student:
    college_name = "Northeastern University" # this is a class attribute cause it is common for all inside the class

    def __init__(self, name):
        self.name = name # this is a object level attribute for each object
        print(name)


s1 = Student("Gaurav")
print(s1.college_name)

# Methods
"""In classes it can store two things. One is data and the other is methods."""