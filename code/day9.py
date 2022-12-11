import numpy as np
test = False
positions = set()
# head = np.array([0, 0])
pieces = []
for i in range(10):
    pieces.append(np.array([0, 0]))
directions = {'R': [1, 0], 'L': [-1, 0], 'U': [0, -1], 'D': [0, 1]}


def update_position(index):
    global pieces
    distance_away = pieces[index] - pieces[index - 1]
    if max(distance_away) > 1 or min(distance_away) < -1:
        if distance_away[0] > 0:
            pieces[index] += directions['L']
        elif distance_away[0] < 0:
            pieces[index] += directions['R']
        if distance_away[1] > 0:
            pieces[index] += directions['U']
        if distance_away[1] < 0:
            pieces[index] += directions['D']


with open('../test_input_files/day9test.txt' if test else '../input_files/day9input.txt','r') as f:
    for line in f:
        direction, distance = line.split()
        for i in range(int(distance)):
            pieces[0] += directions[direction]
            for i in range(1, 10):
                update_position(i)
            positions.add(tuple(pieces[-1]))
print(len(positions))
