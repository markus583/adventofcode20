import numpy as np
import itertools

with open('data/5.csv', 'r') as f:
    text = f.read()

binary = text.replace('B', '1')
binary_2 = binary.replace('F', '0')
binary_3 = binary_2.replace('R', '1')
binary_4 = binary_3.replace('L', '0')
max = 0
splitat = 7
seatlist = []
for line in binary_4.split('\n'):
    row = line[:splitat]
    row = '0b' + row
    column = line[splitat:]
    column = '0b' + column
    row_dec = int(row, 2)
    column_dec = int(column, 2)
    id = (row_dec * 8) + column_dec
    if id > max:
        max = id
    seatlist.append([row_dec, column_dec])


def takeSecond(elem):
    return elem[0]


seatlist.sort(key=takeSecond)

#print(seatlist)
all_rows = range(2, 104)
all_columns = range(8)
all_seats = list(itertools.product(all_rows, all_columns))
seatlist_copy = []

for seat in all_seats:
    seatlist_copy.append(list(seat))
for seat in all_seats:
    seat = list(seat)
    if seat in seatlist:
        seatlist_copy.remove(seat)

my_id = (seatlist_copy[0][0] * 8) + seatlist_copy[0][1]
print(seatlist_copy, my_id)

