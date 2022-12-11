import numpy as np

grid = []
test = False
with open('../test_input_files/day8test.txt' if test else '../input_files/day8input.txt','r') as f:
    for line in f:
        line = line.rstrip()
        grid.append([int(x) for x in line])

grid = np.array(grid)
HEIGHT = len(grid)
LENGTH = len(grid[0])
total = 0

for x in range(HEIGHT):
    for y in range(LENGTH):
        tree = grid[x, y]
        visible = False
        for direction in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
            direction_good = True
            new_x = x
            new_y = y
            while True:
                new_x += direction[0]
                new_y += direction[1]
                if not (0 <= new_x < HEIGHT and 0 <= new_y < LENGTH):
                    break
                if tree <= grid[new_x, new_y]:
                    direction_good = False
            visible |= direction_good
        if visible:
            total += 1

print(total)


import numpy as np

grid = []
test = False
with open('../test_input_files/day8test.txt' if test else '../input_files/day8input.txt','r') as f:
    for line in f:
        line = line.rstrip()
        grid.append([int(x) for x in line])

grid = np.array(grid)
HEIGHT = len(grid)
LENGTH = len(grid[0])
totals = []
for x in range(HEIGHT):
    for y in range(LENGTH):
        total = 1
        tree = grid[x, y]
        for direction in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
            dir_total = 0
            new_x = x
            new_y = y
            while True:
                new_x += direction[0]
                new_y += direction[1]
                if not (0 <= new_x < HEIGHT and 0 <= new_y < LENGTH):
                    break
                if tree <= grid[new_x, new_y]:
                    dir_total += 1
                    break
                dir_total += 1
            total *= dir_total
        totals.append(total)
print(max(totals))
