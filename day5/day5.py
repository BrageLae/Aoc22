import os
from math import floor
from copy import deepcopy

FILE = 'input.txt'
path = os.path.dirname(__file__)

with open(os.path.join(path, FILE)) as f:
    lines = f.readlines()

count = 0

for line in lines:
    if line == '\n':
        break
    count += 1

stack_amount = int((lines[count-1].strip())[-1])

list_of_stacks = []
for i in range(stack_amount):
    list_of_stacks.append([])

for line in lines[:count-1]:
    i = 0
    for char in line:
        i += 1
        if char.isalpha():
            list_of_stacks[floor(i/4)].insert(0, char)

list_of_stacks_2 = deepcopy(list_of_stacks)
# list_of_stacks_tst = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

for line in lines[count+1:]:
    operations = []
    line = line.split()
    for word in line:
        if word.isnumeric():
            operations.append(int(word))
    assert(len(operations) == 3)
    move_amount = operations[0]
    from_stack = operations[1] - 1
    to_stack = operations[2] - 1
    list_of_stacks_2[to_stack].extend(list_of_stacks_2[from_stack][-move_amount:])
    while(move_amount > 0):
        list_of_stacks[to_stack].append(list_of_stacks[from_stack].pop())
        list_of_stacks_2[from_stack].pop()
        move_amount -= 1

print(''.join([stack[-1] for stack in list_of_stacks]))
print(''.join([stack[-1] for stack in list_of_stacks_2]))
