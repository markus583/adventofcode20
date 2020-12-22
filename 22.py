def part_a(text):
    player_1 = []
    for line in text.split('\n'):
        if line.startswith('Player'):
            continue
        elif line == '':
            break
        else:
            player_1.append(int(line))

    player_2 = []
    player_2_turn = False
    for line in text.split('\n'):
        if line.startswith('Player 2'):
            player_2_turn = True
            continue
        if player_2_turn:
            player_2.append(int(line))

    index = 0
    while True:
        index += 1
        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)
        if card_1 > card_2:
            player_1.append(card_1)
            player_1.append(card_2)
        elif card_2 > card_1:
            player_2.append(card_2)
            player_2.append(card_1)

        if len(player_2) == 0 or len(player_1) == 0:
            break

    sum = 0
    if len(player_1) > 1:
        for index, number in enumerate(player_1[::-1], start=1):
            sum += index * number
    else:
        for index, number in enumerate(player_2[::-1], start=1):
            sum += index * number

    return sum


if __name__ == '__main__':
    with open('data/22.txt', 'r') as f:
        text = f.read()
    solution_a = part_a(text)
    print(solution_a)
