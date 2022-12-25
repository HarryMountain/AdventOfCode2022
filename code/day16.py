from copy import deepcopy
no_useful_valves = 0
test = True
valves = {}
with open('../test_input_files/day16test.txt' if test else '../input_files/day16input.txt','r') as f:
    for line in f:
        data = line.rstrip().split()
        id = data[1]
        flow_rate = int(data[4].split('=')[1].split(';')[0])
        tunnels = [x[:-1] if x[-1] == ',' else x for x in data[9:]]
        valves[id] = [flow_rate, tunnels]
        if flow_rate > 0:
            no_useful_valves += 1

states = [['AA', set(), 0]]
for i in range(30):
    print(i)
    print(len(states))
    new_states = []
    for state in states:
        if len(state[1]) >= no_useful_valves:
            new_score = state[2]
            for valve in state[1]:
                new_score += valves[valve][0]
            new_states.append([state[0], state[1], new_score])
        else:
            if valves[state[0]][0] > 0:
                if state[0] in state[1]:
                    new_score = state[2]
                    new_valves = state[1] + state[0]
                    for valve in new_valves:
                        new_score += valves[valve][0]
                    new_states.append([state[0], new_valves, new_score])
            for new_valve in valves[state[0]][1]:
                new_score = state[2]
                for valve in state[1]:
                    new_score += valves[valve][0]
                new_states.append([new_valve, state[1], new_score])
    '''
    length = len(new_states)
    index = 0
    while index < length:
        removed = False
        new_state = new_states[index]
        for check_state in new_states:
            if check_state != new_state:
                if new_state[0] == check_state[0]:
                    if new_state[1].issubset(check_state[1]) and new_state[2] <= check_state[2]:
                        new_states.pop(index)
                        length -= 1
                        removed = True
        if not removed:
            index += 1
    '''
    states = new_states
print(states)

