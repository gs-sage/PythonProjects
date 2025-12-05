# This program checks if a number is a multiple of 7

userInput = int(input("Enter a number: "))

if(userInput%7==0):
    print(f"{userInput} is multiple of 7.")
else:
    print(f"{userInput} is not a multiple of 7.")