raw_input()
raw_input()

import sys, collections

used, avail = {}, {}

for line in sys.stdin:
    line = line.strip().split()
    x, y = map(lambda x:int(x[1:]), line[0].split('-')[1:])
    u = int(line[2][:-1])
    a = int(line[3][:-1])
    used[(x,y)] = u
    avail[(x,y)] = a
    #print x, y, u, a

for (ax,ay), u in used.items():
    for (bx,by), a in avail.items():
        if ax == bx and ay == by: continue
        if u != 0 and u <= a:
            print (ax, ay), (bx, by), u, a

def swap((x,y)):
    return y,x

for (y, x), u in sorted(map(lambda x: (swap(x[0]), x[1]), used.items())):
    if x == 0: print
    print u,
print

for (y, x), u in sorted(map(lambda x: (swap(x[0]), x[1]), avail.items())):
    if x == 0: print
    print u,
print 
