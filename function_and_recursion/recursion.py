"""Recursion is when a function calls itself repeatedly.
Every work done by loops can be done by recursion and every work done
by recursion can be done by loops."""

def print_num(num): # my custom function that prints numbers
    if(num==0): # logic to stop when number is 0
        return
    print(num) # printing the number 
    print_num(num-1) # calling the function inside the function 


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




