# this program finds the highest number from 3 numbers
# typed by the user

userInput1 = float(input("Enter first number: "))
userInput2 = float(input("Enter second number: "))
userInput3 = float(input("Enter third number: "))

if(userInput1>userInput2 and userInput1>userInput3):
    print(f"Highest Number; {userInput1}")
elif(userInput2>userInput1 and userInput2>userInput3):
    print(f"Highest Number: {userInput2}")
else:
    print(f"Highest Number: {userInput3}")
