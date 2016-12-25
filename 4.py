import sys
from collections import defaultdict

swap = lambda x: (x[1], x[0])
def rot(s, n):
    result = ''
    for c in s:
        if not c.isalpha():
            result += c
            continue
        c = ord(c)
        c -= ord('a')
        c += n
        c %= 26
        c += ord('a')
        c = chr(c)
        result += c
    return result
    
n = 0
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    line = line.rsplit('[')
    line, checksum = line[0], line[1].strip(']')
    roomname, sid = line.rsplit('-', 1)
    sid = int(sid)
    ls = defaultdict(int)
    for c in roomname:
        if c == '-': continue
        ls[c] += 1

    ls = sorted(ls.items(), key = lambda v: (-v[1], v[0]))
    if checksum == ''.join([l[0] for l in ls])[:5]:
        print sid, rot(roomname, sid)
        n += sid

print n
