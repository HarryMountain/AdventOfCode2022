import numpy as np
test = False
cycle = 0
x = 1
values = [0, 0, 0, 0, 0, 0]
with open('../test_input_files/day10test.txt' if test else '../input_files/day10input.txt','r') as f:
    for line in f:   
        data = line.split()
        if data[0] == 'noop':
            cycle += 1
        else:
            cycle += 2
            x += int(data[1])
        if 0 in values:
            value_to_check = values.index(0)
            if value_to_check == 0:
                index_to_check = 20
            else:
                index_to_check = value_to_check * 40 + 20
            if len(data) > 1:
                x_add = int(data[1])
            else:
                x_add = 0
            if cycle == index_to_check:
                values[value_to_check] = (x - x_add) * cycle
            elif cycle > index_to_check:
                values[value_to_check] = (x - x_add) * (cycle - 1)
print(sum(values))


def draw_at_position(index, x):
    global grid
    if -2 < index - (x + (index // 40) * 40) < 2:
        grid[index // 40, index % 40] = '#'


test = False
x = 1
grid = np.array([['.'] * 40] * 6)
print(grid)
index = 0
with open('../test_input_files/day10test.txt' if test else '../input_files/day10input.txt','r') as f:
    for line in f:
        data = line.split()
        if data[0] == 'noop':
            draw_at_position(index, x)
            index += 1
        else:
            draw_at_position(index, x)
            draw_at_position(index + 1, x)
            index += 2
            x += int(data[1])
for line in grid:
    print(*line,sep='')



