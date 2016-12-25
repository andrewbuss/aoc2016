x = list('abcdefgh')

import sys
for line in sys.stdin:
    line = line.strip().split()
    if line[1] == 'right':
        dist = int(line[2])
        x = x[dist:] + x[:dist]
    elif line[1] == 'left':
        dist = int(line[2])
        x = x[:-dist] + x[-dist:]
    elif line[:1] == ['swap', 'letter']:
        a, b = line[2], line[5]
        x[x.index(a)], x[x.index(b)] = b, a
    elif line[:1] == ['swap','position']
        
