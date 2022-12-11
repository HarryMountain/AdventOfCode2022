test = False
with open('../test_input_files/day6test.txt' if test else '../input_files/day6input.txt','r') as f:
    current = []
    data = f.readline()
    for i in range(len(data)):
        current.append(data[i])
        if len(current) == 14:
            check = set(current)
            if len(check) == 14:
                print(i + 1)
            current.pop(0)

        