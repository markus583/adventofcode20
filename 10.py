import numpy as np
from functools import lru_cache

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

print(counter)
print(f'{(counter[0]) * counter[2]}')


@lru_cache(maxsize=None)
def dfs(g, u, t): return 1 if u == t else sum(dfs(g, c, t) for c in range(u + 1, u + 4) if c in g)


def solve(data):
    data += [max(data) + 3]
    return dfs(tuple(data), 0, max(data))


solution = solve(numbers)
print(solution)
