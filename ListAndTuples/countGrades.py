# program that counts the number of occurences of a grade in a tuple

grade = ("C","D","A","A","B","B","A")

userInput = input("Enter a grade to see how many students have it(A-F): ").upper()

print(f"{grade.count(userInput)} students have grade {userInput}.")