import os 

class Monkey():
    number_of_monkeys = 0
    reduction = 1

    def __init__(self, items, operation, test):
        self.starting = [item for item in items]
        self.items = items
        self.operation = operation 
        self.test = test
        self.times_inspected = 0
        self.name = Monkey.number_of_monkeys
        Monkey.number_of_monkeys += 1
        Monkey.reduction *= test

    def get_name(self):
        return self.name

    def add_next_monkeys(self, next_a, next_b):
        self.next_a = next_a
        self.next_b = next_b

    def inspect_all(self):
        size = len(self.items)
        for i in range(size):
            self.items[i] = eval(self.operation, {"old":self.items[i]})
        self.times_inspected += size

    def bored_all(self):
        self.items = [item // 3 for item in self.items]

    def send_all(self):
        while len(self.items) > 0:
            item = self.items.pop()
            if item % self.test == 0:
                self.next_a.items.append(item)
            else:
                self.next_b.items.append(item)

    def reset(self):
        self.items = self.starting
        self.times_inspected = 0

    def reduce(self):
        self.items = [item % Monkey.reduction for item in self.items]

    def __repr__(self):
        return f"Monkey {self.name}: {self.items}"
        
FILE = "input.txt"
ROUNDS = 20
ROUNDS_2 = 10_000
path = os.path.dirname(__file__)

with open(os.path.join(path, FILE)) as f:
    lines = f.readlines()
    
monkeys = []
next_monkeys = []
for line in lines:
    if line.lstrip().startswith("Starting"):
        starting = ''.join(char for char in line if char.isdigit() or char.isspace())
        starting = [int(item) for item in starting.split()]
    elif line.lstrip().startswith("Operation"):
        operation = line[line.find("old"):].strip()
    elif line.lstrip().startswith("Test"):
        test = int(''.join([char for char in line if char.isdigit()]))
    elif line.lstrip().startswith("If true"):
        next_a = int(''.join([char for char in line if char.isdigit()]))
    elif line.lstrip().startswith("If false"):
        next_b = int(''.join([char for char in line if char.isdigit()]))
        monkeys.append(Monkey(starting, operation, test))
        next_monkeys.append((next_a, next_b))

for monkey, (next_a, next_b) in zip(monkeys, next_monkeys):
    for m in monkeys:
        if(m.get_name() == next_a):
            monkey_a = m
        if(m.get_name() == next_b):
            monkey_b = m
    monkey.add_next_monkeys(monkey_a, monkey_b)

for round in range(ROUNDS):
    print(f"ROUND {round+1}: ")
    for monkey in monkeys:
        monkey.inspect_all()
        monkey.bored_all()
        monkey.send_all()
    for monkey in monkeys:
        print(monkey)

def puzzle_answer(monkeys):
    activity = [monkey.times_inspected for monkey in monkeys]

    out = 1
    for x in sorted(activity, reverse=True)[:2]:
        out *= x
    print(out)
    
puzzle_answer(monkeys)

for monkey in monkeys:
    monkey.reset()

prints = [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

for rounds in range(ROUNDS_2):
    for monkey in monkeys:
        monkey.inspect_all()
        monkey.reduce()
        monkey.send_all()
    if(rounds + 1 in prints):
        print(f"== After round {rounds + 1} ==")
        for monkey in monkeys:
            print(f"Monkey {monkey.name}: inspected items {monkey.times_inspected} times.")

puzzle_answer(monkeys)