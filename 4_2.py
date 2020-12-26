import re

with open('data/4.csv', 'r') as f:
    text = f.read()

text = text.split('\n\n')

counter = 0
pattern_byr = 'byr:'
pattern_iyr = 'iyr:'
pattern_eyr = 'eyr:'
pattern_hgt = 'hgt:'
pattern_hcl = 'hcl:'
pattern_ecl = 'ecl:'
pattern_pid = 'pid:'
pattern_list = [pattern_byr, pattern_iyr, pattern_eyr, pattern_hgt, pattern_hcl, pattern_ecl, pattern_pid]
for entry in text:
    pattern_counter = 0
    for pattern in pattern_list:
        match_list = re.search(pattern, entry)
        if match_list is not None:
            pattern_counter += 1
        if pattern_counter == len(pattern_list):
            counter += 1

print(counter)