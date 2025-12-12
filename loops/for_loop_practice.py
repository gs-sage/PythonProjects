# print numbers from 1 to 100:

for i in range(1,101):
    print(i)

print()

# print numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)

# print multiplication table of a number
user_input = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{user_input} x {i} = {user_input * i}")


"""Pass Statement is a null statement that does nothing, it is used as a
placeholder for future code. Only used when we don't want nothing there for 
the moment"""

for i in range(5):
    # leaving it empty
    pass

# pass can also be used in if-else statements
if(i>5):
    pass

