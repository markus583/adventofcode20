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
    out_array = np.copy(state)
    # pad input state with zeros
    padded_state = np.pad(state, 1)

    # loop over all rows
    for row_index, row in enumerate(padded_state):
        # exclude padding
        if 1 <= row_index < (len(padded_state) - 1):
            # loop over all columns
            for cell_index, cell in enumerate(row):
                # exclude padding
                if 1 <= cell_index < (len(row) - 1):
                    # get sum of neighbors a cell currently has
                    counter = 0
                    list = [padded_state[row_index - 1, cell_index], padded_state[row_index, cell_index - 1],
                         padded_state[row_index, cell_index + 1], padded_state[row_index + 1, cell_index],
                         padded_state[row_index - 1, cell_index - 1], padded_state[row_index + 1, cell_index - 1],
                         padded_state[row_index - 1, cell_index + 1], padded_state[row_index + 1, cell_index + 1]]
                    for element in list:
                        if element == '#':
                            counter += 1
                    # if current cell is live cell
                    if state[row_index - 1, cell_index - 1] == 'L' and counter == 0:
                        out_array[row_index - 1, cell_index - 1] = '#'
                    # if current cell is dead cell
                    if state[row_index - 1, cell_index - 1] == '#' and counter >= 4:
                        out_array[row_index - 1, cell_index - 1] = 'L'
    return out_array


if __name__ == '__main__':
    with open('11.txt', 'r') as f:
        text = f.read()


    def split(word):
        return [char for char in word]


    # transform initial state seed into numpy array consisting of 1's and 0's
    seed_list = [char for char in (line for line in text.splitlines()) if char]
    new_list = [split(line) for line in seed_list]
    array = np.asarray(new_list)
    state = __get_next_state__(array)
    list = [state]
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