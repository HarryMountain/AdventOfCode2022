test = False
stacks = []
for i in range(3 if test else 9):
    stacks.append([])
with open('../test_input_files/day5test.txt' if test else '../input_files/day5input.txt','r') as f:
    for line in f:
        if '[' in line:
            for i in range(1, len(line), 4):
                if line[i] != ' ':
                    stacks[(i - 1) // 4].insert(0, line[i])
        elif 'move' in line:
            data = line.split()
            number = int(data[1])
            start = int(data[3]) - 1
            end = int(data[5]) - 1
            # for i in range(number):
            #     value = stacks[start].pop(-1)
            #     stacks[end].append(value)
            stacks[end].extend(stacks[start][(-number):])
            stacks[start] = stacks[start][:-number]
print(*[x[-1] for x in stacks], sep='')