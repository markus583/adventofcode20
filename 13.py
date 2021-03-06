from sympy import symbols, solve, Eq
import numpy as np


def processing(data, retain_x=False):
    lines = data.split('\n')
    timestamp = int(lines[0])
    if not retain_x:
        id_list = [int(number) for number in lines[1].split(',') if number != 'x']
    elif retain_x:
        id_list = [int(number) if number != 'x' else 'x' for number in lines[1].split(',')]
    return timestamp, id_list


def get_times(timestamp, id_list):
    x = symbols('x')
    first_arrival = []
    for id in id_list:
        eq1 = Eq(id * x, timestamp)
        time = int(solve(eq1)[0]) * id + id
        first_arrival.append(time)
    return first_arrival


def loop(buses, timestamp=0):
    lowest = buses[0]
    x = symbols('x')
    while True:
        time_counter = 0
        unordered_list = [timestamp]
        sorted_list = []
        for index, bus in enumerate(buses):
            if index == 0:
                time_counter += 1
                sorted_list.append(timestamp + index)
                continue
            if bus != 'x':
                sorted_list.append(timestamp + index)
                timestamp_2 = timestamp
                equation = Eq(bus * x, timestamp_2)
                current_time = int((solve(equation)[0] + 0.5)) * bus
                unordered_list.append(current_time)
                if unordered_list[-1] > unordered_list[-2]:
                    break
            time_counter += 1
        if sorted_list == unordered_list:
            return timestamp, unordered_list
        timestamp += lowest
        if timestamp % 1000 == 0:
            print(timestamp)


# part 1
# my solution is 3865
if __name__ == '__main__':
    with open('data/13.txt', 'r') as f:
        text = f.read()
    timestamp, id_list = processing(text)
    solutions = get_times(timestamp, id_list)
    dict = dict(zip(solutions, id_list))
    min = np.min(solutions)
    print(f'Solution for part 1 is: {(min - timestamp) * dict[min]}')


# part 2
# my solution is 415579909629976
if __name__ == '__main__':
    with open('data/13.txt', 'r') as f:
        text = f.read()
    _, id_list = processing(text)
    _, id_list_with_x = processing(text, retain_x=True)
    timestamp, _ = loop(id_list_with_x)
    print(f'Solution for part 2 is {timestamp}')

