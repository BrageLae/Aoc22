import os 

FILE = 'input.txt'
path = os.path.dirname(__file__)

tail_visited = set()
tail_visited_2 = set()

directions = {'R' : [1,0],
              'L' : [-1,0],
              'U' : [0,1],
              'D' : [0,-1]
}

tail_position = [0,0]
head_position = [0,0]
rope_position_2 = [[0,0] for _ in range(9)]

with open(os.path.join(path, FILE)) as f:
    lines = f.readlines()

def move_tail(tp, hp):
    move_x, move_y = 0, 0
    delta_x = hp[0] - tp[0]
    delta_y = hp[1] - tp[1]

    if delta_x not in [-1,0,1]:
        move_x += delta_x // abs(delta_x)
        if delta_y != 0:
            move_y += delta_y // abs(delta_y)
    elif delta_y not in [-1,0,1]:
        move_y += delta_y // abs(delta_y)
        if delta_x != 0:
            move_x += delta_x // abs(delta_x)
    
    tp[0] += move_x; tp[1] += move_y

    return tp


for line in lines:
    direction, steps = line.strip().split()
    for i in range(int(steps)):
        head_position[0] += directions.get(direction)[0]; head_position[1] += directions.get(direction)[1]
        tail_position = move_tail(tail_position, head_position)
        tail_visited.add(tuple(tail_position))

        """2:"""
        for j in range(len(rope_position_2)):
            if j == 0: 
                hp = head_position
            else: 
                hp = rope_position_2[j-1]
            rope_position_2[j] = move_tail(rope_position_2[j], hp)
        tail_visited_2.add(tuple(rope_position_2[-1]))

print(len(tail_visited))
print(len(tail_visited_2))



