# creating a simple program with class, constructors that takes student name, marks of 3 subjects and a method
# that provides the average of the 3 subject marks.

class Student():
    def __init__(self, name, marks_one, marks_two, marks_three):
        self.name = name 
        self.marks_one = marks_one
        self.marks_two = marks_two
        self.marks_three = marks_three
        print(name)

    def avg_marks(self):
        avg_marks = (self.marks_one + self.marks_two + self.marks_three) / 3
        return avg_marks
    

s1 = Student("Gaurav",98,85,99)
print(s1.avg_marks())