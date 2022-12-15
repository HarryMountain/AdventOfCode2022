test = False
row_to_check = 10 if test else 2000000
sensors = {}
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


blocked_positions = set()
for sensor, beacon in sensors.items():
    dist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    y_diff = abs(row_to_check - sensor[1])
    x_dist = dist - y_diff
    for x in range(sensor[0] - x_dist, sensor[0] + x_dist + 1):
        blocked_positions.add(x)

for beacon in sensors.values():
    if beacon[1] == row_to_check:
        if beacon[0] in blocked_positions:
            blocked_positions.remove(beacon[0])

print(len(blocked_positions))
