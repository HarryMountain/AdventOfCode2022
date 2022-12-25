test = False
number_to_index = []
with open('../test_input_files/day20test.txt' if test else '../input_files/day20input.txt','r') as f:
    index = 0
    for line in f:
        if line != '\n':
            number = int(line)
            number_to_index.append([number * 811589153, index])
        index += 1
length = len(number_to_index)
for cycle in range(10):
    for i in range(length):
        for j in range(length):
            if number_to_index[j][1] == i:
                new_position = (number_to_index[j][0] + j) % (length - 1)
                data = number_to_index.pop(j)
                number_to_index.insert(new_position, data)
                break
    print(cycle)

zero_index = 0
for i in range(length):
    if number_to_index[i][0] == 0:
        zero_index = i
        break

print(number_to_index)
print(sum([number_to_index[(zero_index + x) % length][0] for x in [1000, 2000, 3000]]))
