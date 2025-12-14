"""Recursion is when a function calls itself repeatedly.
Every work done by loops can be done by recursion and every work done
by recursion can be done by loops."""

def print_num(num): # my custom function that prints numbers
    if(num==0): # logic to stop when number is 0
        return
    print(num) # printing the number 
    print_num(num-1) # calling the function inside the function 
    #print("END") # this will print for each stack of the function, uncomment to check


print_num(5)

"""first step is it checks if the number is 0
print 5
it is a calling a function print_num(4)
print 4
print(3)
print 3
3-1=2
print 2
print_num(1)
print 1
print_num(0)
"""

"""Function calls work as a call stack in memory

|                   |
|                   |
|                   |
|3rd here           |
|2nd here           |
|1st call takes space here -- the way it works is for each recursion call a new stack is made in memory
|___________________|    

so after the logic where the if statement is true, function goes back to each stack
and checks if any work is left cause right before the last statement, the function
kept on being called, so after recursion ends, it prints or does any remaining work after for
each call stack. So, in the above function where we print END at the end, will only print
for each function call before the num value was equal to 0 after the value reaches 0 for num.
"""





