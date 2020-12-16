def part_a(text):
    array = []
    for index, line in enumerate(text.split('\n')):
        if line == '':
            break
        # get 2-word features and store in list
        if index < 10:
            split_line = line.split(' ')
            range_1 = split_line[2].split('-')
            range_2 = split_line[4].split('-')
            list_1 = list(range(int(range_1[0]), int(range_1[1]) + 1))
            array.append(list_1)
            list_2 = list(range(int(range_2[0]), int(range_2[1]) + 1))
            array.append(list_2)
        # get 1-word features and store in list
        else:
            split_line = line.split(' ')
            range_1 = split_line[1].split('-')
            range_2 = split_line[3].split('-')
            list_1 = list(range(int(range_1[0]), int(range_1[1]) + 1))
            array.append(list_1)
            list_2 = list(range(int(range_2[0]), int(range_2[1]) + 1))
            array.append(list_2)

    # flatten list
    flat_array = [item for sublist in array for item in sublist]
    bad_array = []
    # check if one of tickets is not in flat_array
    for index, line in enumerate(text.split('\n')):
        if index > 24:
            numbers = line.split(',')
            for number in numbers:
                if int(number) not in flat_array:
                    bad_array.append(int(number))
    return sum(bad_array)


if __name__ == '__main__':
    with open('data/16.txt', 'r') as f:
        text = f.read()
    out = part_a(text)
    print(out)
