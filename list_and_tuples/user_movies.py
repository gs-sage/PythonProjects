# program to ask user for 3 movies as input and add them to a list

# creating an empty list
movie_list = []

# asking for user input
movie_one = input("Enter first movie: ")
movie_two = input("Enter second movie: ")
movie_three = input("Enter third movie: ")

# appending user inputs to the empty list
movie_list.append(movie_one) 
movie_list.append(movie_two)
movie_list.append(movie_three)
print(movie_list)