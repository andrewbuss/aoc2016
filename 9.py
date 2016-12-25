import sys
from collections import defaultdict, Counter

d = sys.stdin.read().strip()

def decompressed_size(x):
    o = 0
    while x:
        if x[0] == '(':
            marker, x = x[1:].split(')',1)
            l, count = map(int, marker.split('x'))
            seq, x = x[:l], x[l:]
            o += decompressed_size(seq) * count
            
        else:
            o += 1
            x = x[1:]
    return o


print decompressed_size(d)
