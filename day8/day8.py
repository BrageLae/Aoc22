import os
import numpy as np

path = os.path.dirname(__file__)
FILE = 'input.txt'

with open(os.path.join(path, FILE)) as f:
    mat = np.array([[char for char in line.strip()] for line in f])

number_invisible = 0
scenic_scores = []

def first_geq(arr, value):
    count = 0
    for item in arr:
        count += 1
        if item >= value:
            return count
    return count

for r in range(1, len(mat) - 1):
    for c in range(1, len(mat[0]) - 1):
        current_height = mat[r,c]
        below = mat[r+1:,c]
        above = np.flip(mat[:r,c])
        right = mat[r,c+1:]
        left = np.flip(mat[r,:c])
        if (max(below) >= current_height and max(above) >= current_height and \
            max(right) >= current_height and max(left) >= current_height):
            number_invisible += 1
        b_view = first_geq(below, current_height)
        a_view = first_geq(above, current_height)
        r_view = first_geq(right, current_height)
        l_view = first_geq(left, current_height)

        scenic_scores.append(b_view*a_view*r_view*l_view)

print((len(mat) * len(mat[0])) - number_invisible)
print(max(scenic_scores))
