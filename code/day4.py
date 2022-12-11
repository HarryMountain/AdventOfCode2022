test = False
total = 0
with open('../test_input_files/day4test.txt' if test else '../input_files/day4input.txt','r') as f:
    for line in f:
        elf1, elf2 = [[int(y) for y in x.split('-')] for x in line.split(',')]
        if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
            total += 1
        elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
            total += 1
print(total)

total = 0
with open('../test_input_files/day4test.txt' if test else '../input_files/day4input.txt','r') as f:
    for line in f:
        elf1, elf2 = [[int(y) for y in x.split('-')] for x in line.split(',')]
        if max([elf1[0], elf2[0]]) <= min([elf1[1], elf2[1]]):
            total += 1
print(total)
        