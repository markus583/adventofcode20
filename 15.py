with open('data/15.txt', 'r') as f:
    text = f.read()

input = [int(number) for number in text.split(',')]
my_dict = dict()

for player, number in enumerate(range(11)):
    if player < len(input):
        my_dict[number] = input[player]
        continue
    current_dict = {v: [k for k in my_dict if my_dict[k] == v] for v in set(my_dict.values())}
    for index, num_player in enumerate(current_dict.values()):
        success = False
        if index + 1 == len(num_player):
            my_dict[number] = 0
            break
        for current_number in num_player:
            if current_number in current_dict.keys():
                if len(num_player) > 1 and my_dict[player - 1] == current_dict[current_number]:
                    my_dict[number] = num_player[-1] - num_player[-2]
                    success = True
                    break


# my_dict[7] = 19
print(my_dict)
