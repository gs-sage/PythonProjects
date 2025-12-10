# program takes input from user for 3 subjects and marks and adds them to a dictionary

# initialize an empty dictionary
student_marks = {}

# taking user inputs
subject1 = input("Enter the subject name: ").capitalize()
marks1 = float(input(f"Enter marks for {subject1}: "))

subject2 = input("Enter the subject name: ").capitalize()
marks2 = float(input(f"Enter marks for {subject2}: "))

subject3 = input("Enter the subject name: ").capitalize()
marks3 = float(input(f"Enter marks for {subject3}: "))

# adding user inputs to dictionary
student_marks.update({subject1:marks1})
student_marks.update({subject2:marks2})
student_marks.update({subject3:marks3})

print(student_marks)