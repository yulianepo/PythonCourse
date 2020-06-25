db = {
    'apple': 'red',
    'lettuce': 'green',
    'lemon': 'yellow',
    'orange': 'orange'
    }
print(db)

name_test = input("please enter a name: ")
pass_test = input("please enter a password: ")

try:
    _ = db[name_test]
    print("Welcome Master")
except KeyError:
    print("INTRUDER ALERT")