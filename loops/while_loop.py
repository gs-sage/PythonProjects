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
        

    



