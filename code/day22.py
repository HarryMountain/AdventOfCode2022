import numpy as np

grid = []
test = False
getting_grid = True
movement = []
with open('../test_input_files/day22test.txt' if test else '../input_files/day22input.txt','r') as f:
    for line in f:
        line = line.rstrip()
        if line == '':
            getting_grid = False
        else:
            if getting_grid:
                grid.append(line)
            else:
                current_number = ''
                for char in line:
                    if char == 'R' or char == 'L':
                        movement.append(int(current_number))
                        movement.append(char)
                        current_number = ''
                    elif char == 'E':
                        movement.append(int(current_number))
                        current_number = ''
                    else:
                        current_number += char

width = max([len(x) for x in grid])
length = len(grid)
maze = np.zeros((length, width), dtype=int)
for line in range(len(grid)):
    for i in range(width):
        if i < len(grid[line]):
            if grid[line][i] == '#':
                maze[line, i] = 1
            elif grid[line][i] == '.':
                maze[line, i] = 0
            else:
                maze[line, i] = -1
        else:
            maze[line, i] = -1

print(maze)
print(movement)

position = [0, 0]
for thing in range(len(maze[0])):
    if maze[0, thing] == 0:
        position[1] = thing
        break

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
direction = 0
for move in movement:
    if isinstance(move, int):
        index = 0
        new_y = position[0]
        new_x = position[1]
        last_good_y = position[0]
        last_good_x = position[1]
        while index < move:
            new_y = (new_y + directions[direction][0]) % length
            new_x = (new_x + directions[direction][1]) % width
            if maze[new_y, new_x] == 0:
                last_good_y = new_y
                last_good_x = new_x
                index += 1
            elif maze[new_y, new_x] == 1:
                break
        position[0] = last_good_y
        position[1] = last_good_x
    else:
        direction = (direction + (1 if move == 'R' else -1)) % 4

print(sum([1000 * (position[0] + 1), 4 * (position[1] + 1), direction]))
