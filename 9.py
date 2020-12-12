from itertools import product
import numpy as np

with open('data/9.txt', 'r') as f:
    text = f.read()

preamble = 25
all_numbers = [int(number) for number in text.split('\n')]
numbers = all_numbers[preamble:]

for index, number in enumerate(numbers):
    success = False
    combinations = list(product(all_numbers[index:index+preamble], all_numbers[index:index+preamble]))
    for (n1, n2) in combinations:
        if n1 == n2:
            continue
        if number == n1 + n2:
            success = True
            break
    if not success:
        print(f'Bad number is {number} at index {index}!')
        bad_number = number
        bad_index = index
        break


for index, number2 in enumerate(all_numbers):
    success = False
    higher_numbers = all_numbers[index+1:]
    var = number2
    list = [number2]
    for higher_number in higher_numbers:
        var += higher_number
        list.append(higher_number)
        if var > bad_number:
            break
        if var == bad_number:
            np_list = np.asarray(list, dtype=np.int64)
            lowest = np.min(np_list)
            highest = np.max(np_list)
            print(f'Sum of highest and lowest number is: {lowest + highest}')
            success = True
            break
    if success:
        break
