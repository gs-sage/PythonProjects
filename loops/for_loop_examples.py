# Some examples of for loop

# print the element in the list
nums = [1,4,9,16,25,36,49,64,81,100]

for num in nums:
    print(num)

print()


# search for a number in the tuple
tup = (1,4,9,16,25,36,49,64,81,100,1,4)

user_input = int(input("Enter a number: "))

idx = 0 # creating a index counter cause we are looping through the elements in for loop and not the index

# looping through the elements in the tuple and not the index
for el in tup:
    if(el == user_input):
        print(f"Number {user_input} found in index {idx}")

    idx+=1 # increasing count of index each time

"""Range function returns a sequence of numbers, starting from 0 by default
and increments by 1(by default) and stops before a specified number.
Range works like range(start, stop, step)"""

for el in range(5): # prints from 0 to 4
    print(el)

for el in range(1,5): # prints from 1 to 4
    print(el)

for el in range(1,6,2): # prints from 1 and increases by 2 step size
    print(el)