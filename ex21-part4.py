import collections


class Clerk:

    def __init__(self, name):
        self.name = name
        self.queue = []

    def add_to_queue(self, *args):
        self.queue += args

    def next_in_queue(self):
        return self.queue.pop(0)

    def print_name(self):
        print(self.name)


### init a list of clerks
list_of_clerks = collections.defaultdict(Clerk)
### the input
while True:
    line = input().split()

    command = line[0]
    if command == 'break':
        break
    name = line[1]
    if name not in list_of_clerks:
        list_of_clerks[name] = Clerk(name)
    if command == 'wait':
        person = line[2]
        list_of_clerks[name].add_to_queue(person)
    elif command == 'next':
        try:
            print(list_of_clerks[name].next_in_queue())
        except IndexError:
            print("No one is in line")

