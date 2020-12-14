from collections import OrderedDict
from itertools import permutations, combinations, product, repeat
import numpy as np


def part_1(text):
    total = 0
    # here, unique addresses will be stored and only the higher index will be retained
    addresses = OrderedDict()
    for e, line in enumerate(text.split('\n')):
        if line.startswith('mem'):
            line_split = line.split(' = ')
            addresses[line_split[0]] = e
    # sort dict
    sorted_addresses = {k: v for k, v in sorted(addresses.items(), key=lambda item: item[1])}

    # loop over all lines
    for index, line in enumerate(text.split('\n')):
        split_line = line.split(' = ')
        # init. current int. value
        counter = 0
        if line.startswith('mask'):
            mask = split_line[1]
        elif line.startswith('mem'):
            # skip over addresses which would've been replaced later
            if sorted_addresses[split_line[0]] != index:
                continue

            raw_address = line[4:9]
            numeric_filter = filter(str.isdigit, raw_address)
            address = "".join(numeric_filter)
            value = int(split_line[1])
            # get list of binary values of current address
            bin_value = bin(value).split('b')[1]
            copy_value = list(bin_value)
            # loop over all entries in mask in reverse order
            for index, binary in enumerate(mask[::-1]):
                # in case binary(address) is smaller than mask
                if len(copy_value) <= index:
                    if mask[-index - 1] == '1':
                        counter += 2 ** index
                    continue
                if mask[-index - 1] == 'X':
                    continue
                elif mask[-index - 1] == '1':
                    copy_value[-index - 1] = '1'
                elif mask[-index - 1] == '0':
                    copy_value[-index - 1] = '0'

            # get int of copy_value
            bin_final = ''.join(map(str, copy_value))
            decimal_value = int(bin_final, 2) + counter
            total += decimal_value
    return total


def part_2(text):
    array = np.empty(shape=55209983983)
    total = 0
    # here, unique addresses will be stored and only the higher index will be retained
    addresses = OrderedDict()
    for e, line in enumerate(text.split('\n')):
        if line.startswith('mem'):
            line_split = line.split(' = ')
            addresses[line_split[0]] = e
    # sort dict
    sorted_addresses = {k: v for k, v in sorted(addresses.items(), key=lambda item: item[1])}

    # loop over all lines
    for index, line in enumerate(text.split('\n')):
        split_line = line.split(' = ')
        # init. current int. value
        counter = 0
        counter_address = 0
        if line.startswith('mask'):
            mask = split_line[1]
        elif line.startswith('mem'):
            # skip over addresses which would've been replaced later
            if sorted_addresses[split_line[0]] != index:
                continue

            raw_address = line[4:9]
            numeric_filter = filter(str.isdigit, raw_address)
            address = "".join(numeric_filter)
            value_address = int(address)
            # get list of binary values of current address
            bin_value_address = bin(value_address).split('b')[1]
            copy_value_address = list(bin_value_address)
            # loop over all entries in mask in reverse order
            for index, binary in enumerate(mask[::-1]):
                # in case binary(address) is smaller than mask
                if len(copy_value_address) <= index:
                    copy_value_address.insert(0, binary)
                    if mask[-index - 1] == '1':
                        counter_address += 2 ** index
                    continue
                if mask[-index - 1] == 'X':
                    copy_value_address[-index - 1] = 'X'
                    continue
                elif mask[-index - 1] == '1':
                    copy_value_address[-index - 1] = '1'

            # get int of copy_value
            bin_final = ''.join(map(str, copy_value_address))
            num_X = bin_final.count('X')
            boolean_list = [1, 0]
            write_addresses = list(product(boolean_list, repeat=num_X))
            memory_list = []
            for c, address in enumerate(write_addresses):
                if c > 0:
                    memory_list.append(local_value_address)
                local_value_address = copy_value_address.copy()
                for d, x in enumerate(address):
                    for index, char in enumerate(local_value_address):
                        if char == 'X':
                            local_value_address[index] = x
                            if c == len(write_addresses) - 1 and d == len(address) - 1:
                                memory_list.append(local_value_address)
                            break

            print(memory_list)
            for memory_address in memory_list:
                bin_final = ''.join(map(str, memory_address))
                decimal_value = int(bin_final, 2)
                array[decimal_value] = int(split_line[1])


    return sum(array)


if __name__ == '__main__':
    with open('data/14.txt', 'r') as f:
        text = f.read()
    solution_1 = part_1(text)
    print(solution_1)
    solution_2 = part_2(text)
    print(solution_2)
