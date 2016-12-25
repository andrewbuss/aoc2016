import sys
from collections import defaultdict

n = 0
is_valid = lambda t: all([t[i-2] + t[i-1] > t[i] for i in range(3)])
ts = defaultdict(list)

for line in sys.stdin:
    line = line.strip().split()
    t = map(int, line)
    for i, v in enumerate(t):
        ts[i].append(v)
    if len(ts[0]) == 3:
        for i in range(3):
            if is_valid(ts[i]):
                n += 1
            del ts[i]
print n
