import re

with open('data/2.csv', 'r') as f:
    file = f.read()

counter = 0

for index, line in enumerate(file.split('\n')):
    if line != '':
        split = line.split(' ')
        bounds = split[0].split('-')
        lower_bound = int(bounds[0])
        upper_bound = int(bounds[1])

        literal = split[1][0]

        current_count = split[2].count(literal)
        print(current_count)

        if upper_bound >= current_count >= lower_bound:
            counter += 1

print(counter)


counter = 0
counter_2 = 0

for index, line in enumerate(file.split('\n')):
    if line != '':
        split = line.split(' ')
        bounds = split[0].split('-')
        lower_bound = int(bounds[0])
        upper_bound = int(bounds[1])

        literal = split[1][0]
        if (split[2][lower_bound - 1] == literal and not split[2][upper_bound - 1] == literal) or (not split[2][lower_bound - 1] == literal and split[2][upper_bound - 1] == literal):
            counter_2 += 1

print(counter_2)

