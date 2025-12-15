# practice examples of recursion

# program that returns the sum of n natural numbers using recursion

# creating a function that provides the sum of n numbers

"""IMPORTANT
Recursion calls keeps happening till the base case is hit.
So in the following example, the calls keep happening till num hits 0.
Once it hits 0, it will return that and add it to the previous call"""
def add_num(num):
    if(num==0):
        return 0
    return add_num(num-1)+num

"""Imagine the above function like this:
add_num(5) -- finally giving value of 15 at the end.
calls add(5-1)+5 -- 5-1=4 whose value is 10 and adding 5 making 15 and sent upwards
calls add(4-1)+4 -- 4-1 is 3 whose value is 6 and adding 4 making 10 and sent upwards
calls add(3-1)+3 -- 3-1 is 2 whose value is 3 and added 3 becoming 6 and sent upwards
calls add(2-1)+2 -- 2-1=1 whose value is 1 and 2 is added becoming 3
calls add(1-1)+1 -- 1-1=0 so now 0+1 is added which is 1 and send upwards
calls add (0) -- hits base case returns 0 and now it sends it back upwards"""

""" So in recursion, once the base logic is hit and return value obtained
the value is sent back for evaluation."""

print(add_num(2))


# creating a recursive function to print elements in a list
def print_list(list, idx):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1) 

new_list = [1,2,3]
print_list(new_list,0)

"""Notes on the above recursive function:
The function takes 2 parameters, a list and an index.
We want the index value to be 0 to start always cause we don't know how big the list may be. 
But we can always keep a logic to stop the function via the len command to get the length of the function.
So, that would also be our base logic to stop the function, once it hits the length of the function stop it, 
otherwise keep adding 1 to the index value.
the first thing the function does is print the value of list at index 0 and then it calls itself, each time
increasing the value of index by 1 till the value of index is equal to the length of the list and then it stops."""
