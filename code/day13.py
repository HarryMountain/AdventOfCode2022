import ast

test = False


def check_order(left, right):
    left_digit = not (type(left) == list)
    right_digit = not (type(right) == list)
    if left_digit:
        left = int(left)
    if right_digit:
        right = int(right)
    if left_digit and right_digit:
        return None if left == right else right > left
    else:
        if left_digit and not right_digit:
            left = [left]
        elif right_digit and not left_digit:
            right = [right]
        index = 0
        ordered = None
        while True:
            if index >= len(left):
                return None if index >= len(right) else True
            elif index >= len(right):
                return False
            check = check_order(left[index], right[index])
            if check is None:
                ordered = None
                index += 1
            else:
                return check
        return ordered



all_packets = []
with open('../test_input_files/day13test.txt' if test else '../input_files/day13input.txt','r') as f:
    for line in f:
        line = line.rstrip()
        if line != '':
            if not line.isdigit():
                line = ast.literal_eval(line)
            all_packets.append(line)

n = len(all_packets)
swapped = False
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if not check_order(all_packets[j], all_packets[j + 1]):
            swapped = True
            all_packets[j], all_packets[j + 1] = all_packets[j + 1], all_packets[j]
    if not swapped:
        break
print(all_packets)

total = 1
for i in range(len(all_packets)):
    if all_packets[i] == [[2]]:
        total *= i + 1
    elif all_packets[i] == [[6]]:
        total *= i + 1
print(total)
