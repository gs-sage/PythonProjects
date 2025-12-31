# creating a simple rock, paper, scissors game for user input and conditionals practice
import random

print("Welcome to Rock, Paper & Scissors Game".center(50, "="))

# One way to do this with lots of if statements and a list
# creating a list for computer input
rps = ["rock","paper","scissor"]

user_input = input("Enter your choice(rock, paper, scissors): ").lower()

computer_input = random.choice(rps)

print(user_input)
print(computer_input)

# Uncomment to test but make sure to comment the second way first to run this part
# if(user_input == "rock" and computer_input == "scissors"):
#     print("user wins")
# elif(user_input == "paper" and computer_input == "rock"):
#     print("user wins")
# elif(user_input == "scissors" and computer_input == "paper"):
#     print("user wins")
# elif(user_input == computer_input):
#     print("It's a draw")
# else:
#     print("computer wins")


# Second way to do this which is cleaner and is more logic proof if needed
# we add a dictionary with predefined winning conditions
wins_against = {
    "rock":"scissors",
    "scissors":"paper",
    "paper":"rock"
}

if(user_input == computer_input):
    print("It's a draw")
# here since we have a dictionary the user input becomes key and gives the value which if is equal to computer input then the user wins
elif(wins_against[user_input] == computer_input): 
    print("user wins")
else:
    print("Computer wins")


