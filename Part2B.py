import sys

sum_grades = 0
high_grades = []
# So the nice thing about sys.argv is that you can use
# list comprehension with it:
# sum_grades = sum([int(i) for i in sys.argv[1:]])
for i in range(1, len(sys.argv)):
    sum_grades += int(sys.argv[i])


avg = sum_grades/len(sys.argv)
print(f" The average grade is: {avg:0.2f} ")

# And list comprehension again...
# high_grades = [g for g in grades if g > avg]
for i in range(1, len(sys.argv)):
    if int(sys.argv[i])> avg:
        high_grades.append(sys.argv[i])
print(high_grades)
