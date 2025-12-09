# program takes a tuple, converts it to list and then sorts it.

grade = ("C","D","A","A","B","B","A")

myList = list(grade) # convertig the tuple to a list

print(f"Unsorted grade: {myList}")

myList.sort() # sorting the list
print(f"Sorted Grade: {myList}")