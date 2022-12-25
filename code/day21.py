import math
from abc import abstractmethod


class Monkey:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def shout(self):
        pass


class NumberMonkey(Monkey):
    def __init__(self, name, number):
        super().__init__(name)
        self.number = number

    def shout(self):
        return [self.number]

    def set_number(self, new_number):
        self.number = new_number


class OperationMonkey(Monkey):
    def __init__(self, name, operation, m1, m2):
        super().__init__(name)
        self.operation = operation
        self.m1 = m1
        self.m2 = m2

    def shout(self):
        m1_shout = monkeys[self.m1].shout()[0]
        m2_shout = monkeys[self.m2].shout()[0]
        value = eval(f"{m1_shout}{self.operation}{m2_shout}")
        return [value, m1_shout, m2_shout]


monkeys = {}
test = False
with open('../test_input_files/day21test.txt' if test else '../input_files/day21input.txt','r') as f:
    for line in f:
        data = line.rstrip().split()
        id = data[0][:-1]
        if len(data) == 2:
            monkeys[id] = NumberMonkey(id, int(data[1]))
        else:
            monkeys[id] = OperationMonkey(id, data[2], data[1], data[3])

check = 3665520865941 - (7012559479583 - 7012559479576.207) // (7012559479576.207 - 7012559479569.422)
good = False
while not good:
    monkeys['humn'].set_number(check)
    result = monkeys['root'].shout()
    if result[0]:
        good = True
    print(result, check)
    check += 1
