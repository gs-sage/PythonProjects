"""For loops are used for sequential traversal like lists, strings, tuples"""

# lists example
list = [1,2,3,4,5]

for num in list:
    print(num)

veggies = ["potato","brinjal","ladyfinger","cucumber"]

for val in veggies:
    print(val)

# tuple example
tup = (1,2,3,4,5,6,2,8,9)

for num in tup:
    print(num)


# String example
str = "Northeastern University"

for char in str:
    print(char)


# for-else example

"""the else only runs if the loop completes. It will not run in cases when
break is used in the loop"""

for char in str:
    if(char=='U'):
        print("U found")
        break
else:
    print("End") # this won't run since we used break

print()

for char in str:
    if(char=="n"):
        print("n found")
        continue
else:
    print("END") # this prints at the end since we use continue