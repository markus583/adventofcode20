def get_number_spoken(input, timestamp):
    # process input
    input = [int(number) for number in input.split(',')]
    my_dict = dict()
    # loop over all players until timestamp
    for player, number in enumerate(range(timestamp)):
        success = False
        # in case of first round
        if player < len(input):
            my_dict[number] = input[player]
            continue
        # find double values
        current_dict = {v: [k for k in my_dict if my_dict[k] == v] for v in set(my_dict.values())}
        keys = list(current_dict.keys())
        values = list(current_dict.values())
        for index, num_player in enumerate(current_dict.values()):
            if success:
                break
            success = False
            for current_number in num_player:
                if len(num_player) > 1 and my_dict[player - 1] == keys[values.index(num_player)]:
                    my_dict[number] = num_player[-1] - num_player[-2]
                    success = True
                    break
                elif 1 == len(num_player):
                    my_dict[number] = 0
    return my_dict[timestamp-1]


if __name__ == '__main__':
    with open('data/15.txt', 'r') as f:
        text = f.read()
    result = get_number_spoken(text, 2020)
    print(result)
