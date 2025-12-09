# Program to check if the number entered by user is odd or even

user_input = int(input("Enter a number: "))

if(user_input>=0):
    if(user_input%2==0):
        print(f"The number {user_input} is even.")
    elif(user_input%2==1):
        print(f"Number {user_input} is odd.")
    else:
        print("Enter a valid number.")
else:
    print("Please enter a positive whole number.")