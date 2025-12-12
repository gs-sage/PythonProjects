# Functions are block of statements that perform a specific task.
# We use functions to decrease redundancy in coding.

#function definition
def calc_sum(a, b): # parameters
    sum = a+b
    print(sum)

calc_sum(5,9) # function call

def calculate_sum(a,b):
    return a+b

print(calculate_sum(1,2))

def print_hello():
    print("Hello")

print_hello()

"""IMPORTANT 
if we try to print a function that doesn't return anything 
it will print None"""

output = print_hello()
print(output) # this will print None

"""Optional things in function
1. Parameter
2. Return"""

# creating a function that provides average of 3 numbers

def average_num(num1,num2,num3):
    average_value = (num1+num2+num3)/3
    return average_value

average_number = average_num(1,2,3)
print(average_number)

num_list = []

def find_avg(list):
    i=0
    sum = 0
    while i<5:
        user_input = float(input("Enter a number: "))
        list.append(user_input)
        i+=1
    
    print(list)

    for j in range(len(list)):
        sum = sum + list[j]
        avg = sum/len(list)
    
    return avg

print(find_avg(num_list))

"""Default Parameters are used when no arguments are passed to a function."""

# assigning default values to arguments in a function
def calc_prod(a=1,b=2): # the default values are 1 and 2 for arguments
    return(a*b)

print(calc_prod()) # will give an output since we have default arguments
    

