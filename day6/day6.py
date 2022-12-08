import os 

FILE = 'input.txt'
path = os.path.dirname(__file__)
MARKER_LENGTH = 4
MSG_MARKER_LENGTH = 14

with open(os.path.join(path, FILE)) as f:
    lines = f.readlines()

def find_pattern(marker_length, line):
    for i in range(marker_length-1, len(line)):
        if len(set(line[i-(marker_length-1):i+1])) == marker_length:
            return(i+1)

for line in lines:
    line.strip()
    print(find_pattern(MARKER_LENGTH, line))

for line in lines:
    line.strip()    
    print(find_pattern(MSG_MARKER_LENGTH, line))