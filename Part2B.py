import sys

sum_grades = 0
high_grades = []
for i in range(1, len(sys.argv)):
    sum_grades += int(sys.argv[i])


avg = sum_grades/len(sys.argv)
print(f" The average grade is: {avg:0.2f} ")

for i in range(1, len(sys.argv)):
    if int(sys.argv[i])> avg:
        high_grades.append(sys.argv[i])
print(high_grades)