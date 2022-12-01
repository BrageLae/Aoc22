FILE = "input.txt"

lst = []
with open(FILE) as f:
    s = 0
    for line in f.readlines():
        if(line != '\n'):
            s += int(line)
        else:
            lst.append(s)
            s = 0
    lst.append(s)

lst.sort()
print(f"Part 1: {lst[-1]}")

print(f"Part 2: {sum(lst[-3:])}, {(lst[-3:])}")

