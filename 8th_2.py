code = []

with open("8.csv") as file:
    for line in file:
        code.append(line)

linesexc = []


def excLine(code, line, acc, changed):
    if line == len(code):
        return True, acc
    if line in linesexc:
        return False, -1
    exc = code[line]
    linesexc.append(line)

    if exc.startswith("n"):
        success, val = excLine(code, line + 1, acc, changed)
        if not success and not changed:
            success, val = excLine(code, line + int(exc[3:]), acc, True)
        if not success:
            linesexc.remove(line)
        return success, val
    if exc.startswith("a"):
        success, val = excLine(code, line + 1, acc + int(exc[3:]), changed)
        if not success:
            linesexc.remove(line)
        return success, val
    if exc.startswith("j"):
        success, val = excLine(code, line + int(exc[3:]), acc, changed)
        if not success and not changed:
            success, val = excLine(code, line + 1, acc, True)
        if not success:
            linesexc.remove(line)
        return success, val


print(excLine(code, 0, 0, False))
