test = False
priority = 0
with open('../test_input_files/day3test.txt' if test else '../input_files/day3input.txt','r') as f:
    for line in f:
        line = line.rstrip()
        line = list(line)
        half = len(line) // 2
        sack1 = set(line[:half])
        sack2 = set(line[half:])
        duplicates = list(sack1.intersection(sack2))
        for duplicate in duplicates:
            ascii_value = ord(duplicate)
            priority += ascii_value - (38 if duplicate.isupper() else 96)
print(priority)

test = False
priority = 0
with open('../test_input_files/day3test.txt' if test else '../input_files/day3input.txt','r') as f:
    group = []
    for line in f:
        line = line.rstrip()
        line = list(line)
        group.append(set(line))
        if len(group) == 3:
            badge = list(group[0].intersection(group[1]).intersection(group[2]))[0]
            ascii_value = ord(badge)
            priority += ascii_value - (38 if badge.isupper() else 96)
            group = []
print(priority)
        