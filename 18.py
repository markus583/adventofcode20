def loop(line):
    operator = ''
    current = 0
    expression = ''
    inside = False
    for index, char in enumerate(line):
        if not inside:
            if char == ' ':
                continue
            elif char.isnumeric():
                new_number = int(char)
                if current == 0:
                    if operator == '+':
                        current = old_number + new_number
                    elif operator == '*':
                        current += old_number * new_number
                elif current != 0:
                    if operator == '+':
                        current += new_number
                    elif operator == '*':
                        current *= new_number
            elif char == '+' or char == '*':
                operator = char
                old_number = new_number

        if inside:
            if char == ')':
                expression += ')'
                new_number = loop(expression)
                inside = False
                expression = ''
                if current == 0:
                    if operator == '+':
                        current = old_number + new_number
                    elif operator == '*':
                        current += old_number * new_number
                    elif operator == '':
                        current = new_number
                elif current != 0:
                    if operator == '+':
                        current += new_number
                    elif operator == '*':
                        current *= new_number
            else:
                expression += char
        if char == '(':
            inside = True
            continue
    return current


if __name__ == '__main__':
    with open('data/18.txt', 'r') as f:
        text = f.read()

    total_a = 0
    for line in text.split('\n'):
        current = loop(line)
        total_a += current
    print(total_a)
