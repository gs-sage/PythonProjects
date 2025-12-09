# program takes a tuple, converts it to list and then sorts it.

grade = ("C","D","A","A","B","B","A")

my_list = list(grade) # convertig the tuple to a list

print(f"Unsorted grade: {my_list}")

my_list.sort() # sorting the list
print(f"Sorted Grade: {my_list}")