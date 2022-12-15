import os 
from anytree import Node, RenderTree

FILE = "input.txt"
path = os.path.dirname(__file__)

with open(os.path.join(path, FILE)) as f:
    lines = f.readlines()

class Value:
    def __init__(self, name : str, value : int = 0):
        self.name = name
        self.value = value
    
    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def is_dir(self):
        if(self.value == 0):
            return True
        return False

    def __repr__(self):
        if(self.value > 0):
            return f"{self.name} (file, size = {self.value})"
        return self.name

root = Node('root')
current_node = root
count = 0
for line in lines:
    count += 1
    line = line.split()
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '/':
                current_node = root
            elif line[2] == '..':
                if(not current_node.is_root):
                    current_node = current_node.parent
            else: # $ cd _
                for i in range(len(current_node.children)):
                    if(current_node.children[i].name.get_name() == line[2]):
                        current_node = current_node.children[i]
                        break
                   
    else:
        if(line[0] == 'dir'):
            node = Node(name = Value(line[1]), parent = current_node)
        else:
            node = Node(name = Value(name = line[1], value = int(line[0])), parent = current_node)
            
print(RenderTree(root))

def size_dir(node, size = 0):
    for child in node.descendants:
        size += child.name.get_value()
    return size

print(sum([size_dir(node) for node in root.descendants if \
    node.name.get_value() == 0 and size_dir(node) <= 100_000]))

current_size = size_dir(root)
needed_space = 30_000_000
total_space = 70_000_000
unused_space = total_space - current_size
minimum_directory_size = needed_space - unused_space

print(min([size_dir(node) for node in root.descendants if \
    node.name.get_value() == 0 and size_dir(node) >= minimum_directory_size]))
