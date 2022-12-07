import os

FILE = 'input.txt'
path = os.path.dirname(__file__)

def binary_search(arr, target):
    l = 0
    r = len(arr) - 1
    while(l <= r):
        m = (l + r) // 2
        if target == arr[m]:
            return m
        elif target < arr[m]:
            r = m - 1
        else:
            l = m + 1
    return -1

def calculate_item_value(item: str):
    if(item.islower()):
        return ord(item) - 96
    return ord(item) - 38


with open (os.path.join(path, FILE)) as f:
    lines = f.readlines()
    lst = [l.strip() for l in lines]

common_items = []
for line in lst:
    compartment_size = len(line)//2
    left_compartment = list(set(line[:compartment_size]))
    right_compartment = list(set(line[compartment_size:]))

    for x in left_compartment:
        if x in right_compartment:
            common_items.append(x)
            break

print(sum([calculate_item_value(item) for item in common_items]))

lst_2 = []
for i in range(3, len(lst)+1, 3):
    lst_2.append(lst[i-3:i])

common_items_2 = []
for threes in lst_2:
    a, b, c = threes
    for x in a:
        if x in b and x in c:
            common_items_2.append(x)
            break

print(sum([calculate_item_value(item) for item in common_items_2]))






        
    