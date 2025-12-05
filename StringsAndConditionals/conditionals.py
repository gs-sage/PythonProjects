"""This program goes over if/elif/else statements"""

age = int(input("Enter your age: "))

if(age>=18):
    print("You are eligible to get a license.")
else:
    print("You are not 18 yet. You can't apply for a license yet.")


# traffic light to understand elif

light = input("Enter the traffic light color: ").capitalize()

if(light == "Green"): # if condition gets checked each time
    print("Go")
elif(light == "Yellow"): # elif only gets checked if, if statement is not valid
    print("Be ready to stop")
else: # only runs if none of the above conditions are true
    print("Stop")

# example of conditionals with a student grade system

# taking input from user for marks
""" This will produce an error and stop the code from moving forward
if the user inputs a string value"""

# Enter the students marks: fg
# Traceback (most recent call last):
#   File "C:\PythonProjects\StringsAndConditionals\conditionals.py", line 26, in <module>
#     userInput = float(input("Enter the students marks: "))
#                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: could not convert string to float: 'fg'


# uncomment this part to try
# userInput = float(input("Enter the students marks: "))

# if(userInput>=90):
#      print("Grade A")
# elif(userInput<90 and userInput>=80):
#     print("Grade B")
# elif(userInput<80 and userInput>=70):
#     print("Grade C")
# elif(userInput<70 and userInput>=60):
#     print("Grade D")
# elif(userInput<60 and userInput>=0):
#     print("Grade F")

# if we use the try-except the code still moves along
""" I also wanted to try, the try-except for any errors.
So the way it works is, in the try block you keep the code that may produce an error.
for this example we kept the user input cause, user can input a string instead of a number.
In those cases, if we don't have the try-except block we get can't conver to string error 
or something along those lines.

With the try-except in place if the error comes up, it prints our statement with the details in one line providing
what caused the error."""

try:
    userInput = float(input("Enter the students marks: "))

    if(userInput>=0):
        if(userInput>=90):
            print("Grade A")
        elif(userInput<90 and userInput>=80):
            print("Grade B")
        elif(userInput<80 and userInput>=70):
            print("Grade C")
        elif(userInput<70 and userInput>=60):
            print("Grade D")
        elif(userInput<60 and userInput>=0):
            print("Grade F")
    else:
        print("Please enter a valid number. ")
except Exception as e:
    print(f"Please enter a valid number. Details: {e}")

print("try-except block works.")