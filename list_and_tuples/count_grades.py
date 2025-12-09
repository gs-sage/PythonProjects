# program that counts the number of occurences of a grade in a tuple

grade = ("C","D","A","A","B","B","A")

user_input = input("Enter a grade to see how many students have it(A-F): ").upper()

print(f"{grade.count(user_input)} students have grade {user_input}.")