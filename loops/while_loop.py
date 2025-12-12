# program that has a bunch of while loops

# print numbers from 1 to 100
print("Printing numbers from 1 to 100")

num = 1
while num<=100:
    print(num)
    num+=1

print()

# print numbers from 100 to 1
print("Printing numbers from 100 to 1")

i = 100
while i>=1:
    print(i)
    i-=1

print()

#  print multiplication table of a number n
print("Print the multiplication of a number")

user_num = int(input("Enter a number: "))
j = 1
while j<=10:
    print(f"{user_num} x {j} = {user_num * j}")
    j+=1

print()

# print the elements of the following list using a loop
print("Printing the elements in the list")

list_num = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i<len(list_num):
    print(list_num[i])
    i+=1

print()

# search for a number in the list using a loop
print("Enter a number to search in the loop")

tuple_num = (1,4,9,16,25,36,49,64,81,100)

search_num = int(input("Enter a number to search: "))

k = 0

while k<len(tuple_num):
    #print(tuple_num[k])
    if(tuple_num[k] != search_num):
        k+=1

    elif(tuple_num[k] == search_num):
        print(f"Your number {search_num} is in the list at index {k}.")
        break
        
print()

"""Break and Continue in loop"""
# Break is used to terminate the loop when encountered
# Continue terminates execution in the current iteration and continues execution of the loop with the next iteration

p = 0
while p<=5:
    if(p==2):
        p+=1
        continue # will skip the rest of the loop parts after this and go to next iteration

    print("Will print when p is not equal to 2 but when it is 2 it will skip")

    if(p==4):
        print("Breaking loop when p is equal to 4 so 4 and 5 won't get printed to output")
        break # this will break the loop and 5 will never get printed

    print(p)
    p+=1

print()

# using while loop and continue to get even and odd numbers
print("Getting even numbers using while loop and continue")

"""IMPORTANT : if we switch the print and the increment places it will print odd and even in the
different loops"""

q=1

# this will get even numbers
while q<=10:
    if(q%2==0):
        q+=1
        continue
    q+=1
    print(q)


# and if we change the if statement to not equla 0 it will print odd numbers

r=1

while r<=10:
    if(r%2!=0):
        r+=1
        continue

    r+=1
    print(r) # prints odd cause we are incrementing before printing
    
