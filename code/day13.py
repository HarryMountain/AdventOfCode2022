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



pair = []
total = 0
index = 1
with open('../test_input_files/day13test.txt' if test else '../input_files/day13input.txt','r') as f:
    for line in f:
        line = line.rstrip()
        if line != '':
            if not line.isdigit():
                line = ast.literal_eval(line)
            pair.append(line)
            if len(pair) == 2:
                if check_order(pair[0], pair[1]):
                    total += index
                    print(index)
                index += 1
                pair = []
print(total)
