# program to ask user for 3 movies as input and add them to a list

# creating an empty list
movieList = []

# asking for user input
movieOne = input("Enter first movie: ")
movieTwo = input("Enter second movie: ")
movieThree = input("Enter third movie: ")

# appending user inputs to the empty list
movieList.append(movieOne) 
movieList.append(movieTwo)
movieList.append(movieThree)
print(movieList)