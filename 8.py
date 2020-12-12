import copy


with open('8.csv', 'r') as f:
    text = f.read()

print(text)

all_lines = text.split('\n')
global_var = 0
position_list = []
position_index = 0


def recursive(all_lines, position, global_var=global_var, position_index=position_index):
    global final_var
    final_var = global_var
    if len(set(position_list)) == len(position_list):
        lines = all_lines[position:]
        for i, line in enumerate(lines):
            if len(set(position_list)) == len(position_list):
                line_split = line.split(' ')
                if line_split[0] == 'acc':
                    current_var = int(line_split[1])
                    global_var += current_var
                    position_index = (i - len(lines) + len(all_lines))
                    position_list.append(position_index)
                elif line_split[0] == 'jmp':
                    position_index = (i - len(lines) + len(all_lines))
                    position_list.append(position_index)
                    jump = int(line_split[1])
                    jumper = i - len(lines) + len(all_lines) + jump

                    final_var = recursive(all_lines, jumper, global_var)
                elif line_split[0] == 'nop':
                    position_index = (i - len(lines) + len(all_lines))
                    position_list.append(position_index)
                    continue
            # global_var += int(local_var)
    # global_var += current_var
    return final_var, position_index


# while not any(x in lines for x in unique_list):

var = recursive(all_lines, 0)
print(var)

global_var = 0
position_list = []
position_index = 0

nop_index = []
jmp_index = []
copy_list = copy.deepcopy(all_lines)
for index, line in enumerate(all_lines):
    if line.startswith('nop'):
        nop_index.append(index)
    elif line.startswith('jmp'):
        jmp_index.append(index)
"""
for index, line in enumerate(all_lines):
    copy_list = copy.deepcopy(all_lines)
    if index in nop_index:
        entry = all_lines[index]
        entry_split = entry.split(' ')
        copy_list[index] = 'jmp ' + entry_split[1]
        copy_list.append('FINAL')


        def recursive(all_lines, position, global_var=global_var, position_index=position_index):
            global final_var
            final_var = global_var
            if copy_list[position_index] == 'FINAL':
                print(index)
            if len(set(position_list)) == len(position_list):
                lines = all_lines[position:]
                for i, line in enumerate(lines):
                    if line == 'FINAL':
                        print(index)
                        break

                    if len(set(position_list)) == len(position_list):
                        line_split = line.split(' ')
                        if line_split[0] == 'acc':
                            current_var = int(line_split[1])
                            global_var += current_var
                            position_index = (i - len(lines) + len(all_lines))
                            position_list.append(position_index)

                        elif line_split[0] == 'jmp':
                            position_index = (i - len(lines) + len(all_lines))
                            position_list.append(position_index)
                            jump = int(line_split[1])
                            jumper = i - len(lines) + len(all_lines) + jump


                            final_var = recursive(all_lines, jumper, global_var)
                        elif line_split[0] == 'nop':
                            position_index = (i - len(lines) + len(all_lines))
                            position_list.append(position_index)
                            continue
                    # global_var += int(local_var)
            # global_var += current_var
            return final_var, position_index
        recursive(copy_list, 0, position_index=0)
"""
global_var = 0
position_list = []
position_index = 0


def recursive_2(all_lines, position, global_var=global_var, position_index=position_index):
    global final_var
    final_var = global_var
    if len(set(position_list)) == len(position_list):
        lines = all_lines[position:]
        for i, line in enumerate(lines):
            if line == 'FINAL' and copy_list[position_index] == 'FINAL':
                print(index, final_var)
            if len(set(position_list)) == len(position_list):
                line_split = line.split(' ')
                position_index = (i - len(lines) + len(all_lines))
                position_list.append(position_index)
                if copy_list[position_index] == 'FINAL':
                    print(index, final_var)
                if line_split[0] == 'acc':
                    current_var = int(line_split[1])
                    global_var += current_var
                    if copy_list[position_index] == 'FINAL':
                        print(index, final_var)
                elif line_split[0] == 'jmp':
                    jump = int(line_split[1])
                    jumper = i - len(lines) + len(all_lines) + jump
                    if copy_list[jumper] == 'FINAL':
                        print(index, final_var)

                    final_var = recursive_2(all_lines, jumper, global_var)
                elif line_split[0] == 'nop':

                    if copy_list[position_index] == 'FINAL':
                        print(index, final_var)
                    continue
            # global_var += int(local_var)
    # global_var += current_var
    return final_var, position_index
copy_list = copy.deepcopy(all_lines)
for index, line in enumerate(all_lines):
    copy_list = copy.deepcopy(all_lines)
    if index in jmp_index:
        entry = all_lines[index]
        entry_split = entry.split(' ')
        copy_list[index] = 'nop ' + entry_split[1]
        copy_list.append('FINAL')


        position_list = []
        recursive_2(copy_list, 0, position_index=0)

for index, line in enumerate(all_lines):
    copy_list = copy.deepcopy(all_lines)
    if index in nop_index:
        entry = all_lines[index]
        entry_split = entry.split(' ')
        copy_list[index] = 'jmp ' + entry_split[1]
        copy_list.append('FINAL')


        position_list = []
        recursive_2(copy_list, 0, position_index=0)

#print(nop_index, jmp_index)