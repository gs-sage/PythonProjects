# this program finds the highest number from 3 numbers
# typed by the user

user_input1 = float(input("Enter first number: "))
user_input2 = float(input("Enter second number: "))
user_input3 = float(input("Enter third number: "))

if(user_input1>user_input2 and user_input1>user_input3):
    print(f"Highest Number; {user_input1}")
elif(user_input2>user_input3):
    print(f"Highest Number: {user_input2}")
else:
    print(f"Highest Number: {user_input3}")
