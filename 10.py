import sys
from collections import defaultdict, Counter

lines = [line.strip().split() for line in sys.stdin if line]

chips = defaultdict(list)
dsts = {}

for line in lines:
    if line[0] == 'value':
        val, bot = map(int, (line[1], line[5]))
        chips[bot].append(val)
    elif line[0] == 'bot':
        ob1, ob2 = line[5], line[6]
        bot, d1, d2 = map(int, (line[1], line[6], line[11]))
        if ob1 == 'output': d1 = -1 - d1
        if ob2 == 'output': d2 = -1 - d2
        dsts[bot] = d1, d2
        print bot, d1, d2

outputs = {}
print "loaded"
compares = {}
while 1:
    moved = False
    for bid in chips:
        if len(chips[bid]) == 2:
            print bid, chips[bid]
            compares[bid] = chips[bid]
            a, b = sorted(chips[bid])
            da, db = dsts[bid]
            assert len(chips[da]) < 2
            assert len(chips[db]) < 2
            if da >= 0: chips[da].append(a)
            else: outputs[-da - 1] = a
            if db >= 0: chips[db].append(b)
            else: outputs[-db - 1] = b
            chips[bid] = []
            moved = True
            break
    if not moved: break
        
print sorted(outputs.items())
print outputs[0] * outputs[1] * outputs[2]
