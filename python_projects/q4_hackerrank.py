"""Task
The provided code stub reads an integer, n, from STDIN. For all non-negative integers i < n, print i squared.

Example
n = 3
The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

0
1
4
Input Format

The first and only line contains the integer, .

Constraints


Output Format

Print  lines, one corresponding to each .

Sample Input 0

5
Sample Output 0

0
1
4
9
16"""

n = int(input("Enter a number: "))
new_list = [] # creating an empty list to add numbers

for i in range(n): # running a loop through the range of the user input
    i = i ** 2 # squaring the value of i in each iteration
    new_list.append(i) # adding i to the empty list
    
for val in new_list: # looping through the new value
    print(val) # finally printing the value to screen

# print(new_list) # had it for debugging purposes

# simpler way I found after researching, the question only asks for one per line and not a list so the below would be best
for i in range(n):
    print(i ** 2)