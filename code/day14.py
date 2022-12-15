blocked_spaces = set()
test = False
highest_y = 0
with open('../test_input_files/day14test.txt' if test else '../input_files/day14input.txt','r') as f:
    for line in f:
        line = [[int(y) for y in x.split(',')] for x in line.rstrip().split(' -> ')]
        position = line.pop(0)
        for location in line:
            num = 1 if location[0] == position[0] else 0
            for i in range(min(position[num], location[num]), max(position[num], location[num]) + 1):
                blocked_position = (location[0], i) if num == 1 else (i, location[1])
                blocked_spaces.add(blocked_position)
                if blocked_position[1] > highest_y:
                    highest_y = blocked_position[1]
            position = location


floor_y = highest_y + 2

for i in range(500 - highest_y - 2, 500 + highest_y + 3):
    blocked_spaces.add((i, floor_y))

blocked = False
sand_at_rest = 0
while not blocked:
    stopped = False
    sand = [500, 0]
    while not stopped:
        x = sand[0]
        y = sand[1]
        if tuple([x, y + 1]) not in blocked_spaces:
            sand[1] += 1
        elif tuple([x - 1, y + 1]) not in blocked_spaces:
            sand[0] -= 1
            sand[1] += 1
        elif tuple([x + 1, y + 1]) not in blocked_spaces:
            sand[0] += 1
            sand[1] += 1
        else:
            stopped = True
            sand_at_rest += 1
            blocked_spaces.add(tuple(sand))
            if sand == [500, 0]:
                print(sand_at_rest)
                blocked = True

