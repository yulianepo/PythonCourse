from random import randint

def read_a_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Sorry! your input isn't a number")


def ex11_part1():
    result = float("-inf")
    for _ in range(0, 10):
        num = read_a_number("Please enter a number: ")
        if num > result:
            result = num
    return result


print(f"the max number is: {ex11_part1()}")


def ex11_part2():
    age = read_a_number("Please enter you age in years: ")
    return age * 12


print(f"your age in months is: {ex11_part2()}")

def ex11_part3():
    texts = ""
    row = input("Please enter a sentence: ")
    while row != "":
        texts = texts + "\n" + row
        row = input("Please enter a sentence: ")
    return texts

"""
try:
    text_list = ex11_part3()
    print(f"{text_list[::-1]}")
except ValueError:
    print("Something went wrong in part 3")
"""

def raise_divide_by_x(num,x):
    if num % x != 0:
        raise Exception("HAHA")


def ex11_part4():
    while True:
        number = randint(1, 1000000)
        try:
            raise_divide_by_x(number, 7)
            raise_divide_by_x(number, 13)
            raise_divide_by_x(number, 15)
            return number
        except Exception:
            pass


print(f"the random number that dives by 7,13,15 is: {ex11_part4()}")

# part 5
def prime_list_func(number):
    prime_list = ""
    for i in list(range(2, number//2+1)):
        try:
            raise_divide_by_x(number, int(i))
            prime_list = prime_list + " " + i
            return prime_list

        except Exception:
            pass


a = prime_list_func(10)
print(f" the prime list is: {a}")


