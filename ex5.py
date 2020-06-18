
"""
# this is part 1

age_years = int(input("how old are you in years? "))
# in python we use spaces around operators, so this:
age_months = age_years * 12
# is better than age_years*12
print(f"you are {age_months} months old")

# this is part 2
age_months = int(input("how old are you in months? "))
age_years = age_months / 12
# This nice trick will trim the output to 2 digits after
# the floating point
print(f"you are {age_years:0.2f} years old")

# this is part 3
number = int(input("please choose a number"))
if number % 7 == 0:
  print("BOOM")

# this is part 4
number = input("please enter a number")
mod7 = 0
contain7 = 0
# So python has an "in" operator which is a bit nicer
# if "7" in number:
#   contain7 = 1
#
for ch in range(len(number)):
  if number[ch]=='7':
    contain7=1

number_int = int(number)
if number_int%7==0:
  mod7=1
if mod7 or contain7:
  print("BOOM")

# So actually what I would write here is:
if "7" in number or int(number) % 7 == 0:
  print("Boom")

# this is part 5
x = int(input("please enter a number1: "))
y = int(input("please enter a number2: "))
z = int(input("please enter a number3: "))
# You don't need the array here:
print("the max value is", max(x, y, z))
"""
# this is part 6
first_element=int(input("please enter the first number in the series: "))
diff = int(input("please enter the diff of the series: "))
num_elements=int(input("please enter the number of elements in series: "))

# Turns out "sum" is a function in python
# (you can see because it's colored in purple)
# It's not too bad to use it as a variable name, but
# it can be confusing. I'd select a different name
sum_series = 0
current_element = first_element
sum_series = sum(range(first_element, last_element, diff))

for i in range(num_elements):
    sum_series += current_element
    current_element += diff
print(sum_series)

