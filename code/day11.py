use_test = False
monkeys = []

class Monkey:
    def __init__(self, items, operation, test, true_monkey, false_monkey):
        self.items = items
        self.operation = operation
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspect_count = 0

    def throw_items(self):
        for old in self.items:
            new = eval(self.operation)
            new = new // 3
            monkeys[self.true_monkey if (new % self.test == 0) else self.false_monkey].items.append(new)
            self.inspect_count += 1
        self.items = []


starting = []
operation = ''
test = 0
true_monkey = 0
false_monkey = 0
with open('../test_input_files/day11test.txt' if use_test else '../input_files/day11input.txt','r') as f:
    for line in f:
        if not line == '\n':
            line = line.strip().split(': ')
            match line[0][0]:
                case 'S':
                    starting = [int(x) for x in line[1].split(', ')]
                case 'O':
                    operation = line[1].split('= ')[1]
                case 'T':
                    test = int(line[1].split()[2])
                case 'I':
                    if line[0].split()[1] == 'true':
                        true_monkey = int(line[1].split()[3])
                    else:
                        false_monkey = int(line[1].split()[3])
                        monkeys.append(Monkey(starting, operation, test, true_monkey, false_monkey))
for i in range(10):
    for monkey in monkeys:
        monkey.throw_items()
    inspect_counts = [m.inspect_count for m in monkeys]
inspect_counts = sorted(inspect_counts, reverse=True)
print(inspect_counts[0] * inspect_counts[1])



