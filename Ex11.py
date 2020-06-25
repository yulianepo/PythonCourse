from random import randint

def read_a_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Sorry! your input isn't a number")


def ex11_part1():
    result = float("-inf")
    # No need to write range(0, 10) -> Can just write range(10)
    for _ in range(0, 10):
        num = read_a_number("Please enter a number: ")
        if num > result:
            result = num
    return result


# print(f"the max number is: {ex11_part1()}")


def ex11_part2():
    age = read_a_number("Please enter you age in years: ")
    return age * 12


# print(f"your age in months is: {ex11_part2()}")

def ex11_part3():
    texts = ""
    row = input("Please enter a sentence: ")
    while row != "":
        # If you put the items in reverse order, you can skip
        # the entire second part of the solution
        # texts = row + "\n" + texts
        texts = texts + "\n" + row
        row = input("Please enter a sentence: ")
    return texts


try:
    text_list = ex11_part3()
    print(f"{text_list[::-1]}")
# This is a bad example of a try/except
# because your except block doesn't do anything productive
# if you can't help - better to let the exception flow until
# someone else could
# (you can also re-raise the exception after printing if that's
#  what you wanted)
# This is called "swallowing" exceptions, and I wrote about it
# here: https://www.tocode.co.il/blog/2018-04-exceptions
except ValueError:
    print("Something went wrong in part 3")


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
def ex11_part5():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    print(num1)
    print(num2)
    small_num = min(num1, num2)
    max_num = max(num1, num2)
    while True:
        try:
            raise_divide_by_x(small_num, num1)
            raise_divide_by_x(small_num, num2)
            return small_num
        except Exception:
            # I think you can increase small_num by itself
            # to make this loop run a bit faster
            # small_num += small_num
            small_num = small_num + 1


print(ex11_part5())

# I see your AI player won't cheat ... that's ok honesty is a virtue
def ex11_part6():
    num = randint(1, 100)
    while True:
        guess = read_a_number("Guess the number: ")
        if guess > num:
            print(" the number you are looking for is smaller")
        elif guess < num:
            print(" the number you are looking for is larger")
        else:
            print("you found the number")
            return


ex11_part6()

