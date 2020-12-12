import math
import numpy as np

with open('12.txt', 'r') as f:
    text = f.read()

lines = text.split('\n')

coords = 0 + 0j
direction = 1 + 0j

for line in lines:
    if line.startswith('S'):
        current_line = int(line.strip('S'))
        coords -= complex(current_line) * 1j
    elif line.startswith('N'):
        current_line = int(line.strip('N'))
        coords += complex(current_line) * 1j
    elif line.startswith('W'):
        current_line = int(line.strip('W'))
        coords -= current_line
    elif line.startswith('E'):
        current_line = int(line.strip('E'))
        coords += current_line
    elif line.startswith('R'):
        current_line = int(line.strip('R'))
        angle = math.radians(current_line)
        direction *= np.round(np.exp(-1j*angle))
    elif line.startswith('L'):
        current_line = int(line.strip('L'))
        angle = math.radians(current_line)
        direction *= np.round(np.exp(1j*angle))
    elif line.startswith('F'):
        current_line = int(line.strip('F'))
        if np.int(direction.imag) == -1:
            coords -= complex(current_line) * 1j
        elif np.int(direction.imag) == 1:
            coords += complex(current_line) * 1j
        elif np.int(direction.real) == -1:
            coords -= current_line
        elif np.int(direction.real) == 1:
            coords += current_line
print(coords)
print(f'{np.abs(coords.real) + np.abs(coords.imag)}')

