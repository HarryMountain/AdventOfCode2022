test = False
total = 0
outcomes = [3, 6, 0]
opponent_dict = {'A': 0, 'B': 1, 'C': 2}
me_dict = {'X': 2, 'Y': 0, 'Z': 1}
with open('../test_input_files/day2test.txt' if test else '../input_files/day2input.txt','r') as f:
    for line in f:
        line = line.rstrip()
        opponent, outcome = line.split()
        opponent = opponent_dict[opponent]
        outcome = me_dict[outcome]
        me = (opponent + outcome) % 3 + 1
        total += me
        total += outcomes[outcome]
        # total += outcomes[(me - opponent) % 3]
        # total += me
print(total)


