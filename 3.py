with open('data/3.csv', 'r') as f:
    text = f.read()


length_line = 0
counter_3 = 0
position_3 = -3

slopes = [1, 3, 5, 7]
for line in text.split('\n'):
    length_line = len(line)
    position_3 += 3
    if position_3 >= length_line:
        position_3 = (position_3 % 30) - 1
    if line[position_3] == '#':
        counter_3 += 1

print('a:', counter_3)

length_line = 0
counter_1 = 0
position_1 = -1

slopes = [1, 3, 5, 7]
for line in text.split('\n'):
    length_line = len(line)
    position_1 += 1
    if position_1 >= length_line:
        position_1 = (position_1 % 30) - 1
    if line[position_1] == '#':
        counter_1 += 1


length_line = 0
counter_5 = 0
position_5 = -5

slopes = [1, 3, 5, 7]
for line in text.split('\n'):
    length_line = len(line)
    position_5 += 5
    if position_5 >= length_line:
        position_5 = (position_5 % 30) - 1
    if line[position_5] == '#':
        counter_5 += 1


length_line = 0
counter_7 = 0
position_7 = -7

slopes = [1, 3, 5, 7]
for line in text.split('\n'):
    length_line = len(line)
    position_7 += 7
    if position_7 >= length_line:
        position_7 = (position_7 % 30) - 1
    if line[position_7] == '#':
        counter_7 += 1




length_line = 0
counter_m1 = 0
position_m1 = -1

slopes = [1, 3, 5, 7]
for i, line in enumerate(text.split('\n')):
    if i % 2 == 0:
        length_line = len(line)
        position_m1 += 1
        if position_m1 >= length_line:
            position_m1 = (position_m1 % 30) - 1
        if line[position_m1] == '#':
            counter_m1 += 1

# print(counter_m1)

print('b:', counter_1 * counter_3 * counter_5 * counter_7 * counter_m1)