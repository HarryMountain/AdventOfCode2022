test = False

elfs = []
with open('../test_input_files/day1test.txt' if test else '../input_files/day1input.txt', 'r') as f:
    current = []
    for line in f:
        line = line.rstrip()
        if len(line) > 0:
            current.append(int(line))
        else:
            elfs.append(sum(current))
            current.clear()
elfs = sorted(elfs, reverse=True)
print(sum([elfs[i] for i in range(3)]))
        