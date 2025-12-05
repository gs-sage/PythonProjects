# Program to check if the number entered by user is odd or even

userInput = int(input("Enter a number: "))

if(userInput>=0):
    if(userInput%2==0):
        print(f"The number {userInput} is even.")
    elif(userInput%2==1):
        print(f"Number {userInput} is odd.")
    else:
        print("Enter a valid number.")
else:
    print("Please enter a positive whole number.")