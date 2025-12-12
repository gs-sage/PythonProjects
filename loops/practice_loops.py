# More practice for loops

# while loop that prints the sum of first n numbers
print("Get the sum of first n number")
user_input = int(input("Enter a number: "))

sum = 0
i = 0

# running while loop for the range of the user input
while i<=user_input:
    print(f"Value of i: {i}") # for debugging purposes
    sum = sum + i # adding value of i to sum in each iteration
    print(f"Value of sum: {sum}") # for debugging
    i+=1

print()
print(f"Final Sum: {sum}") # printing final sum value
print()

# for loop to get factorial of a number
print("Find the Factorial")
user_input2 = int(input("Enter a number: "))

final_factorial = 1 # factorials means we are multiplying so if we use 0 the whole value becomes 0 so we use 1

for j in range(1, (user_input2+1)):
    print(f"Current final factorial: {final_factorial}") # for debugging
    print(f"Current J value: {j}") # for debugging
    final_factorial = final_factorial * j # multiplying the iteration number to final factorial in each iteration

print(f"Final Factorial current: {final_factorial}")

