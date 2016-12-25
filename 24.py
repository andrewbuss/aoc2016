import sys

map = []
ns = {}
for y, line in enumerate(sys.stdin):
    l = []
    for x, c in enumerate(line.strip()):
        if c == ".": l.append(True)
        elif c.isdigit():
            l.append(True)
            ns[int(c)] = (x, y)
        else: l.append(False)
    map.append(l)

from collections import defaultdict
dist_between = defaultdict(dict)
for n in range(len(ns)):
    by_dist = [[ns[n]]]
    by_sq = {}
    d = 1
    while by_dist[-1]:
        by_dist.append(set())
        for (x,y) in by_dist[d-1]:
            if (x,y) in by_sq: continue
            by_sq[(x, y)] = d - 1
            by_dist[d].add((x-1, y))
            by_dist[d].add((x, y-1))
            by_dist[d].add((x+1, y))
            by_dist[d].add((x, y+1))
        by_dist[d] = filter(lambda (x,y): map[y][x] and (x,y) not in by_sq, by_dist[d])
        d += 1
    print by_dist
    for m in ns:
        print n, m
        dist_between[n][m] = by_sq[ns[m]]

print dist_between

from itertools import permutations

def dist(xs):
    if len(xs) == 1:
        return dist_between[0][xs[0]]
    else:
        return dist_between[xs[-1]][xs[-2]] + dist(xs[:-1])

result = 123456
for p in permutations(range(1, len(ns))):
    p = list(p) + [0]
    d = dist(p)
    result = min(result, d)
    print p, d

print result
