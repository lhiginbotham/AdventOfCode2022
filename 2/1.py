inp = []
with open('input.txt') as f:
    inp = f.readlines()
    for i in range(0, len(inp)):
        inp[i] = inp[i].rstrip()

round_scores = []
r = 1
p = 2
s = 3

l = 0
d = 3
w = 6

for match in inp:
    opp, me = match.split()
    if opp == 'A':
        if me == 'X':
            round_scores.append(r + d)
        elif me == 'Y':
            round_scores.append(p + w)
        elif me == 'Z':
            round_scores.append(s + l)
    elif opp == 'B':
        if me == 'X':
            round_scores.append(r + l)
        elif me == 'Y':
            round_scores.append(p + d)
        elif me == 'Z':
            round_scores.append(s + w)
    elif opp == 'C':
        if me == 'X':
            round_scores.append(r + w)
        elif me == 'Y':
            round_scores.append(p + l)
        elif me == 'Z':
            round_scores.append(s + d)

print(sum(round_scores))
