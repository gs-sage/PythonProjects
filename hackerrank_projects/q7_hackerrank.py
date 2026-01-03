# creating an empty list to hold values
student = []

for i in range(int(input())):
    name = input()
    score = float(input())
    student.append([name, score])

print(student)

scores = [score[1] for score in student]
lowest = min(scores)

print(scores)
print(lowest)

above_lowest = [ascore for ascore in scores if ascore > lowest]
second_lowest = min(above_lowest)

print(above_lowest)
print(second_lowest)

student_name = []

for i in student:
    if(i[1] == second_lowest):
        student_name.append[i[0]]

for n in sorted(student_name):
    print(n)