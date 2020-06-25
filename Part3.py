import sys

print("This is the name of the program:", sys.argv[0])

print("Argument List:", str(sys.argv))

db = {}
with open('host.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        key, value = line.split('=')
        db[key] = value
print(db)
# So we actually don't need "i" here:
for hostname in sys.argv[1:]
    try:
        print(f"the IP of {hostname} is: {db[hostname]}")
    except KeyError:
        print(f"for {hostname} no such IP")


for i in range(1, len(sys.argv)):
    try:
        print(f"the IP of {sys.argv[i]} is: {db[sys.argv[i]]}")
    except KeyError:
        print(f"for {sys.argv[i]} no such IP")



