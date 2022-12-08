import os

FILE = 'test_input.txt'

path = os.path.dirname(__file__)

with open(os.path.join(path, FILE)) as f:
    lines = f.readlines()
    lines = [[x.split('-') for x in line.strip().split(',')] for line in lines]

count = 0
count2 = 0
for pair in lines:
    a, b = pair 
    range_a = set(range(int(a[0]), int(a[1])+1))
    range_b = set(range(int(b[0]), int(b[1])+1))
    if range_a.issubset(range_b) or range_b.issubset(range_a):
        count += 1
    if not range_a.isdisjoint(range_b) :
        count2 += 1

print(count, count2)

