with open('data/6.csv', 'r') as f:
    text = f.read()

text = text.split('\n\n')
#print(text)
counter = 0
current_list = []
for group in text:
    current_list = []
    for line in group.split('\n'):
        #print(line)
        for char in line:
            current_list.append(char)
            #print(current_list)
    current_list = list(set(current_list))
    counter += len(current_list)
print(counter)


counter = 0
current_list = []
for group in text:
    current_list = []
    final_list = []
    num_persons = len(group.split('\n'))
    for i, line in enumerate(group.split('\n')):
        current_charlist = []
        for char in line:
            current_charlist.append(char)
            #print(current_list)
        current_charlist = list(set(current_charlist))
        current_list.append(current_charlist)
    final_list = set.intersection(*[set(x) for x in current_list])
    counter += len(final_list)

print(counter)