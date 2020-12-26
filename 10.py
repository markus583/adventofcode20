import numpy as np

with open('data/10.txt', 'r') as f:
    text = f.read()

numbers = [int(line) for line in text.split('\n')]
numbers.append(0)
numbers.sort()
counter = np.zeros(shape=3, dtype=np.int64)

for index, number in enumerate(numbers):
    if number == numbers[-1]:
        counter[2] += 1
        break
    if number + 1 == numbers[index + 1]:
        counter[0] += 1
        continue
    elif number + 2 == numbers[index + 1]:
        counter[1] += 1
        continue
    elif number + 3 == numbers[index + 1]:
        counter[2] += 1
        continue

print(f'{(counter[0]) * counter[2]}')


