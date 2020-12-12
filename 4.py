import re

with open('4.csv', 'r') as f:
    text = f.read()

text = text.split('\n\n')

counter: int = 0
pattern_byr = 'byr:[0-9]+'
pattern_iyr = 'iyr:[0-9]+'
pattern_eyr = 'eyr:[0-9]+'
pattern_hgt = 'hgt:[0-9]+([cm]+|[in]+)'
pattern_hcl = 'hcl:#[\da-f]+'
pattern_ecl = 'ecl:(amb|blu|brn|gry|grn|hzl|oth)+'
pattern_pid = 'pid:(\d){9}'
pattern_list = [pattern_byr, pattern_iyr, pattern_eyr, pattern_hgt, pattern_hcl, pattern_ecl, pattern_pid]
for entry in text:
    pattern_counter = 0
    for i, pattern in enumerate(pattern_list):
        match_list = re.search(pattern, entry)
        if match_list is not None:
            feature = match_list.group(0)
            if i == 0 or i == 1 or i == 2:
                feature_list = feature.split(':')
                if i == 0:
                    if not (1920 <= int(feature_list[1]) <= 2002) or len(feature_list[1]) != 4:
                        continue
                elif i == 1:
                    if not (2010 <= int(feature_list[1]) <= 2020) or len(feature_list[1]) != 4:
                        continue
                elif i == 2:
                    if not (2020 <= int(feature_list[1]) <= 2030) or len(feature_list[1]) != 4:
                        continue
            elif i == 3:
                unit_pattern = '(in)|(cm)'
                height_match = re.search(unit_pattern, pattern)
                if height_match is not None:
                    unit = height_match.group(0)
                    size_pattern = r'\d+'
                    size_match = re.search(size_pattern, feature)
                    size = size_match.group(0)
                    size = int(size)
                    if unit == 'cm':
                        if not (150 <= size <= 193):
                            continue
                    elif unit == 'in':
                        if not (59 <= size <= 76):
                            continue
            elif i == 4:
                color_list = feature.split('#')
                color = color_list[1]
                if len(color) != 6:
                    continue

            pattern_counter += 1

        if pattern_counter == len(pattern_list):
            counter += 1

print(counter)