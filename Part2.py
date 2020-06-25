import sys


grades = []
sum_grades = 0
for i in range(0,3):
    grade = int(input("Please enter a grade: "))
    grades.append(grade)
    sum_grades += grade
print(grades)
avg = sum_grades/len(grades)
print(f" The average grade is: {avg:0.2f} ")


high_grades = [g for g in grades if g > avg]
print(high_grades)
