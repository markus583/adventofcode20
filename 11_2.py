import numpy as np


def __get_next_state__(state) -> np.ndarray:
    """
    Computes the next game state from old game state.
    Live cells = 1.
    Dead cells = 0.

    :param state: initial game state as 2D np array of type np.int
    :return: out_array: np.ndarray with next computed state
    """
    # create np.array with same shape as input state
    global special_row_index
    out_array = np.copy(state)
    # pad input state with zeros
    padded_state = np.pad(state, 1)

    # loop over all rows
    for row_index, row in enumerate(padded_state):
        # exclude padding
        if 1 <= row_index < (len(padded_state) - 1):
            # loop over all columns
            cell_index: int
            for cell_index, cell in enumerate(row):
                # exclude padding
                if 1 <= cell_index < (len(row) - 1):
                    # get sum of neighbors a cell currently has
                    counter = 0
                    list = [0, 0, 0, 0, 0, 0, 0, 0]

                    # row above, then below
                    for special_row_index, row_2 in enumerate(padded_state):
                        if 1 <= special_row_index < (len(row_2) - 1):
                            if special_row_index < row_index:
                                if padded_state[special_row_index, cell_index] == '#':
                                    list[0] = '#'
                                    break
                                elif padded_state[special_row_index, cell_index] == 'L':
                                    list[0] = 'L'
                                    break
                            if special_row_index > row_index:
                                if padded_state[special_row_index, cell_index] == '#':
                                    list[3] = '#'
                                    break
                                elif padded_state[special_row_index, cell_index] == 'L':
                                    list[3] = 'L'
                                    break
                    # columns below and above
                    padded_transpose = np.transpose(padded_state)
                    for special_column_index, column_2 in enumerate(padded_transpose):
                        if 1 <= special_column_index < (len(column_2) - 1):
                            if special_row_index < row_index:
                                if padded_state[special_column_index, row_index] == '#':
                                    list[1] = '#'
                                    break
                                elif padded_state[special_column_index, row_index] == 'L':
                                    list[1] = 'L'
                                    break
                            if special_column_index > row_index:
                                if padded_state[special_column_index, row_index] == '#':
                                    list[2] = '#'
                                    break
                                elif padded_state[special_column_index, row_index] == 'L':
                                    list[2] = 'L'
                                    break

                    # -1, -1
                    special_cell_index = cell_index
                    now_padded = padded_state[:row_index + 1]
                    for diag_1_index, diag_1 in enumerate(now_padded[::-1]):
                        special_cell_index -= 1
                        if special_cell_index < 0:
                            break
                        if padded_state[diag_1_index, special_cell_index] == '#':
                            list[4] = '#'
                            break
                        elif padded_state[diag_1_index, special_cell_index] == 'L':
                            list[4] = 'L'
                            break

                    # -1, + 1
                    special_cell_index_2 = cell_index
                    diag_2_index = row_index
                    now_padded = padded_state[:row_index + 1]
                    for diag_1 in now_padded[::-1]:
                        special_cell_index_2 += 1
                        diag_2_index -= 1
                        if diag_2_index >= 0:
                            if special_cell_index_2 >= len(now_padded[0]) - 1:
                                break
                            if padded_state[diag_2_index, special_cell_index_2] == '#':
                                list[6] = '#'
                                break
                            elif padded_state[diag_2_index, special_cell_index_2] == 'L':
                                list[6] = 'L'
                                break

                    # +1, +1
                    next_cell_index_2 = cell_index
                    diag_3_index = row_index
                    next_padded = padded_state[row_index + 1:]
                    for diag_3 in next_padded:
                        next_cell_index_2 += 1
                        diag_3_index += 1
                        if next_cell_index_2 < len(diag_3):
                            if padded_state[diag_3_index, next_cell_index_2] == '#':
                                list[7] = '#'
                                break
                            elif padded_state[diag_3_index, next_cell_index_2] == 'L':
                                list[7] = 'L'
                                break

                    # +1, -1
                    final_cell_index_2 = cell_index
                    diag_4_index = row_index
                    nextest_padded = padded_state[row_index + 1:]
                    for diag_4 in nextest_padded:
                        final_cell_index_2 -= 1
                        diag_4_index += 1
                        if final_cell_index_2 >= 0:
                            if padded_state[diag_4_index, final_cell_index_2] == '#':
                                list[5] = '#'
                                break
                            elif padded_state[diag_4_index, final_cell_index_2] == 'L':
                                list[5] = 'L'
                                break

                    for element in list:
                        if element == '#':
                            counter += 1
                    # if current cell is live cell
                    if state[row_index - 1, cell_index - 1] == 'L' and counter == 0:
                        out_array[row_index - 1, cell_index - 1] = '#'
                    # if current cell is dead cell
                    if state[row_index - 1, cell_index - 1] == '#' and counter >= 5:
                        out_array[row_index - 1, cell_index - 1] = 'L'
    return out_array


if __name__ == '__main__':
    with open('11_2.txt', 'r') as f:
        text = f.read()


    def split(word):
        return [char for char in word]


    # transform initial state seed into numpy array consisting of 1's and 0's
    seed_list = [char for char in (line for line in text.splitlines()) if char]
    new_list = [split(line) for line in seed_list]
    array = np.asarray(new_list)
    state = __get_next_state__(array)
    list = [state]
    print(__get_next_state__(state))
    while True:
        list.append(__get_next_state__(list[-1]))
        comparison = list[-1] == list[-2]
        if comparison.all():
            print(list[-1])
            final_list = list[-1]
            break

c = 0
for row in final_list:
    for column in row:
        if column == '#':
            c += 1
print(c)
