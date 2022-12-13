import numpy as np
test = False
grid = []
with open('../test_input_files/day12test.txt' if test else '../input_files/day12input.txt','r') as f:
    for line in f:
        line = line.rstrip()
        grid.append(list(line))

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
           start = (i, j)
        if grid[i][j] == 'E':
            end = (i, j)

starts = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'a':
            starts.append((i, j))
grid[start[0]][start[1]] = 'a'
grid[end[0]][end[1]] = 'z'


def steps_to_goal(start, lowest_step):
    step = 0
    done = False
    paths = set()
    paths.add(start)
    while not done:
        new_paths = set()
        for path in paths:
            for direction in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                new_x = direction[0] + path[0]
                new_y = direction[1] + path[1]
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                    if ord(grid[new_x][new_y]) - ord(grid[path[0]][path[1]]) < 2:
                        if grid[new_x][new_y] != 'a':
                            new_paths.add((new_x, new_y))
        step += 1
        paths = new_paths
        if end in paths:
            done = True
        if start in paths:
            paths.remove(start)
        if lowest_step < step:
            return None
    return step

steps = []
index = 0
lowest_step = len(grid) * len(grid[0])
print(len(starts))
for start in starts:
    print(index)
    new_step = steps_to_goal(start, lowest_step)
    if new_step is not None:
        steps.append(new_step)
    index += 1
    lowest_step = min(steps)
print(min(steps))
