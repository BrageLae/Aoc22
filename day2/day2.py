import os 

FILE = "input.txt"
path = os.path.dirname(__file__)

score = 0
score2 = 0
opponents = []; players = []

player_score = {'X':1,
                'Y':2,
                'Z':3}
opp_score = {'A':1,
             'B':2,
             'C':3}

draws = ['AX','BY','CZ']
wins = ['AY','BZ','CX']

"""loss2 = ['AX','BX','CX'] # 3, 1, 2      1+2, 2+2, 3+2
draws2 = ['AY','BY','CY'] # 1, 2, 3
wins2 = ['AZ','BZ','CZ'] # 2, 3, 1      1+1, 2+1, 3+1"""

with open(os.path.join(path,FILE)) as f:
    for line in f.readlines():
        opponent, player = line.split()
        opponents.append(opponent)
        players.append(player)

for opponent, player in zip(opponents, players):
    score += player_score.get(player)
    if opponent+player in draws:
        score += 3
    elif opponent+player in wins:
        score += 6
print(score)

DRAW = 3
WIN = 6

for opponent, outcome in zip(opponents, players):
    s = 0
    if outcome == 'X':
        s = opp_score.get(opponent) + 2
        if s > 3:
            s = s % 3
        score2 += s
    if outcome == 'Y':
        s = opp_score.get(opponent)
        score2 += DRAW + s
    if outcome == 'Z':
        s = opp_score.get(opponent) + 1
        if s > 3:
            s = s % 3
        score2 += WIN + s


print(score2)
