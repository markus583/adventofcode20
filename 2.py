import re

with open('Untitled 1.csv', 'r') as f:
    file = f.read()

counter = 0

for index, line in enumerate(file.split('\n')):
    if line != '':
        #print(line)
        split = line.split(' ')
        #print(split[0])
        bounds = split[0].split('-')
        #print(bounds)
        lower_bound = int(bounds[0])
        upper_bound = int(bounds[1])
        #print(lower_bound)

        literal = split[1][0]
        print(literal)

        current_count = split[2].count(literal)
        print(current_count)

        if current_count <= upper_bound and current_count >= lower_bound:
            counter += 1

print(counter)


counter = 0
counter_2 = 0

for index, line in enumerate(file.split('\n')):
    if line != '':
        #print(line)
        split = line.split(' ')
        #print(split[0])
        bounds = split[0].split('-')
        #print(bounds)
        lower_bound = int(bounds[0])
        upper_bound = int(bounds[1])
        #print(lower_bound)

        literal = split[1][0]
        #print(literal)

        if (split[2][lower_bound - 1] == literal and not split[2][upper_bound - 1] == literal) or (not split[2][lower_bound - 1] == literal and split[2][upper_bound - 1] == literal):
            counter_2 += 1

print(counter_2)

