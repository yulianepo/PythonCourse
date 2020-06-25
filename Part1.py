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
    # I can see why this is cool, but I don't like it
    # because it's hard to read. A program should tell a
    # story. An asssignment operator says "I'm setting
    # something to be something", but that's not what you
    # do here.
    # Also you test only half the story: That the user is in DB
    # but he may be using a wrong password
    _ = db[name_test]
    print("Welcome Master")
except KeyError:
    print("INTRUDER ALERT")
