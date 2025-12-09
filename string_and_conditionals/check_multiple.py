# This program checks if a number is a multiple of 7

user_input = int(input("Enter a number: "))

if(user_input%7==0):
    print(f"{user_input} is multiple of 7.")
else:
    print(f"{user_input} is not a multiple of 7.")