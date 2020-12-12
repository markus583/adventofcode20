import math
import numpy as np

with open('data/12.txt', 'r') as f:
    text = f.read()

lines = text.split('\n')

# we use imaginery numbers, where East/West is the real axis and North/South the complex
coords = 0 + 0j
direction = 1 + 0j
waypoint = 10 + 1j

# now the waypoint is moving
for line in lines:
    if line.startswith('S'):
        current_line = int(line.strip('S'))
        waypoint -= complex(current_line) * 1j
    elif line.startswith('N'):
        current_line = int(line.strip('N'))
        waypoint += complex(current_line) * 1j
    elif line.startswith('W'):
        current_line = int(line.strip('W'))
        waypoint -= current_line
    elif line.startswith('E'):
        current_line = int(line.strip('E'))
        waypoint += current_line
    elif line.startswith('R'):
        current_line = int(line.strip('R'))
        angle = math.radians(current_line)
        waypoint *= np.round(np.exp(-1j*angle))
    elif line.startswith('L'):
        current_line = int(line.strip('L'))
        angle = math.radians(current_line)
        waypoint *= np.round(np.exp(1j*angle))
    elif line.startswith('F'):
        current_line = int(line.strip('F'))
        coords += waypoint * current_line
print(coords)
print(f'{np.abs(coords.real) + np.abs(coords.imag)}')

