from  itertools import combinations

with open('data/1.txt', newline='') as f:
    text = f.read()

data = text.split('\r\n')
all_feature_pairs = list(combinations(data, 2))
correct_answer = []
for (one, two) in all_feature_pairs:
    one_proc = int(one[0])
    two_proc = int(two[0])
    if one_proc + two_proc == 2020:
        correct_answer = [one_proc, two_proc]
        break


print(f'{one_proc} + {two_proc} = 2020, which was our goal.\nFinally, {one_proc} * {two_proc} = {one_proc * two_proc}!')


data[0][0] = '2008'
all_feature_pairs = list(combinations(data, 3))
correct_answer = []
for (one, two, three) in all_feature_pairs:
    one_proc = int(one[0])
    two_proc = int(two[0])
    three_proc = int(three[0])

    if one_proc + two_proc + three_proc == 2020:
        correct_answer = [one_proc, two_proc, three_proc]
        break

print(correct_answer)
print(f'{one_proc * two_proc * three_proc}')