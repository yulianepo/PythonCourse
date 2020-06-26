class Summer:
    def __init__(self):
        self._sum = 0

    def add(self, *args):
        for num in args:
            self._sum += num

    def print_total(self):
        print(self._sum)


s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
s.print_total()

# should print 50
t.print_total()

"""
def print_for(*args):
    print(args)
    for i in args:
        print(i)


print_for(1,2,3)
print_for(1,2,3,4)
"""