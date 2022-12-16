import copy
test = False
sensors = {}
bounds = 20 if test else 4000000
with open('../test_input_files/day15test.txt' if test else '../input_files/day15input.txt','r') as f:
    for line in f:   
        sense, beac = line.rstrip().split(':')
        sensor_data = sense.split(', ')
        beacon_data = beac.split(', ')
        sensor_x = int(sensor_data[0].split()[2].split('=')[1])
        sensor_y = int(sensor_data[1].split('=')[1])
        beacon_x = int(beacon_data[0].split()[4].split('=')[1])
        beacon_y = int(beacon_data[1].split('=')[1])
        sensor_pos = (sensor_x, sensor_y)
        beacon_pos = (beacon_x, beacon_y)
        sensors[sensor_pos] = beacon_pos


def get_range_on_row(row_to_check):
    ranges = []
    for sensor, beacon in sensors.items():
        dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        y_diff = abs(row_to_check - sensor[1])
        x_dist = dist - y_diff
        if x_dist >= 0:
            ranges.append((sensor[0] - x_dist, sensor[0] + x_dist))
    return sorted(ranges)


def work_out_overlaps(ranges, start_index):
    for i in range(start_index, len(ranges) - 1):
        if ranges[i][1] >= ranges[i + 1][0] - 1:
            new_start = ranges[i][0]
            new_end = max(ranges[i + 1][1], ranges[i][1])
            ranges[i] = (new_start, new_end)
            ranges.pop(i + 1)
            return work_out_overlaps(ranges, i)
    return ranges


for row in range(bounds):
    if row % 10000 == 0:
        print(row)
    ranges = get_range_on_row(row)
    merged = work_out_overlaps(ranges, 0)
    if len(merged) > 1:
        print(row, merged)

x = 2829680 * 4000000
y = 3411840
print(x + y)
