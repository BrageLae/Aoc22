import os

path = os.path.dirname(__file__)
FILE = 'input.txt'

with open(os.path.join(path, FILE)) as f:
    lines = f.readlines()

cycles = [20, 60, 100, 140, 180, 220]
pc = 0
register_X = 1
sprite = [0,1,2]
signal_strengths = []
crt = []
    
def signal_strength(pc):
    if(len(cycles) > 0 and pc >= cycles[0]):
        return cycles.pop(0) * register_X
    return 0

def draw(pc, sprite):
    newline = ''
    sign = '.'
    if (pc % 40) in sprite:
        sign = '#'
    if(pc % 40 == 0):
        newline = '\n'
    return (newline + sign)


for line in lines:
    line = line.strip().split()
    if(line[0] == 'addx'):
        crt.append(draw(pc, sprite))
        crt.append(draw(pc+1, sprite))
        pc += 2
        signal_strengths.append(signal_strength(pc))
        register_X += int(line[1])
        sprite = [register_X-1, register_X, register_X+1]
    else:
        crt.append(draw(pc,sprite))
        pc += 1
        signal_strengths.append(signal_strength(pc))

print(sum([signal for signal in signal_strengths]))
print(''.join(crt))
