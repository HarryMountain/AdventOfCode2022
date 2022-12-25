from copy import deepcopy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

test = False
cubes = []
with open('../test_input_files/day18test.txt' if test else '../input_files/day18input.txt','r') as f:
    for line in f:
        cube = [int(x) for x in line.rstrip().split(',')]
        cubes.append(cube)

'''
total = len(cubes) * 6
for cube in cubes:
    for cube2 in cubes:
        if cube != cube2:
            coords = [0, 0, 0]
            for coord in range(3):
                diff = abs(cube[coord] - cube2[coord])
                if diff == 1:
                    coords[coord] = 1
                elif diff == 0:
                    coords[coord] = 0
                else:
                    coords[coord] = -1
            if sum(coords) == 1 and -1 not in coords:
                total -= 1

print('WOWOWOWOWOWOWOWOWOW')
'''

directions = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]


def flood_fill(start):
    inside = [start]
    stuff_to_check = [start]
    stuff_to_add = []
    added = True
    while added:
        added = False
        for cube in stuff_to_check:
            for direction in directions:
                new_cube = [cube[x] + direction[x] for x in range(3)]
                if new_cube not in cubes + inside + stuff_to_add:
                    stuff_to_add.append(new_cube)
                    added = True
        stuff_to_check = deepcopy(stuff_to_add)
        inside.extend(deepcopy(stuff_to_add))
        # print(stuff_to_add)
        stuff_to_add = []
        # print(len(inside))
        if len(inside) > 1301:
            return False
    return True


inside = []
for i in range(len(cubes)):
    print(i)
    cube = cubes[i]
    for direction in directions:
        new_cube = [cube[x] + direction[x] for x in range(3)]
        if new_cube not in cubes and new_cube not in inside:
            direction_checks = [False, False, False, False, False, False]
            for check in cubes:
                if check[0] == cube[0] and check[1] == cube[1]:
                    if check[2] > cube[2]:
                        direction_checks[4] = True
                    else:
                        direction_checks[5] = True
                elif check[0] == cube[0] and check[2] == cube[2]:
                    if check[1] > cube[1]:
                        direction_checks[2] = True
                    else:
                        direction_checks[3] = True
                elif check[1] == cube[1] and check[2] == cube[2]:
                    if check[0] > cube[0]:
                        direction_checks[0] = True
                    else:
                        direction_checks[1] = True
            if sum(direction_checks) == 6 and flood_fill(new_cube):
                inside.append(new_cube)

print('WOWOOWOWOWO', len(inside))


result = len(cubes) * 6
for cube in cubes:
    for cube2 in cubes + inside:
        if cube != cube2:
            coords = [0, 0, 0]
            for coord in range(3):
                diff = abs(cube[coord] - cube2[coord])
                if diff == 1:
                    coords[coord] = 1
                elif diff == 0:
                    coords[coord] = 0
                else:
                    coords[coord] = -1
            if sum(coords) == 1 and -1 not in coords:
                result -= 1

plot = True
if plot:
    highest_on_axis = (max([x[0] for x in cubes]) + 1, max([y[1] for y in cubes]) + 1, max([z[2] for z in cubes]) + 1)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    voxels = np.zeros(highest_on_axis)
    colors = np.empty(voxels.shape, dtype=object)
    for cube in cubes:
        voxels[cube[0], cube[1], cube[2]] = True
        colors[cube[0], cube[1], cube[2]] = [1, 1, 0, 0.4]
    for cube in inside:
        voxels[cube[0], cube[1], cube[2]] = True
        colors[cube[0], cube[1], cube[2]] = [0, 1, 0, 0.8]
    ax.voxels(voxels, edgecolor="black", facecolors=colors)
    plt.axis = [0, max(highest_on_axis), 0, max(highest_on_axis), 0, max(highest_on_axis)]
    plt.show()
    # print(total)
    print(result)
