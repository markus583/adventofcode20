from itertools import product
import numpy as np

with open('9.txt', 'r') as f:
    text = f.read()

all_numbers = text.split('\n')
numbers = all_numbers[25:]

for index, number in enumerate(numbers):
    success = False
    combinations = list(product(all_numbers[:index+25], all_numbers[:index+25]))
    for (n1, n2) in combinations:
        if n1 == n2:
            continue
        if int(number) == int(n1) + int(n2):
            success = True
            break
    if not success:
        print(f'Bad number is {number} at index {index}!')
        bad_number = number
        bad_index = index
        break


for index, number in enumerate(numbers):
    success = False
    higher_numbers = numbers[index+1:]
    var = int(number)
    list = [number]
    for higher_number in higher_numbers:
        var += int(higher_number)
        list.append(higher_number)
        if var > bad_number:
            break
        if var == bad_number:
            list = [int(element) for element in list]
            np_list = np.asarray(list, dtype=np.int64)
            lowest = np.min(np_list)
            highest = np.max(np_list)
            print(f'Sum of highest and lowest number is: {lowest + highest}')
            success = True
            break
    if success:
        break
