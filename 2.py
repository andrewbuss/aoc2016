import sys
keys = {
    (2,0) : '1',
    (1,1) : '2',
    (2,1) : '3',
    (3,1) : '4',
    (0,2) : '5',
    (1,2) : '6',
    (2,2) : '7',
    (3,2) : '8',
    (4,2) : '9',
    (1,3) : 'A',
    (2,3) : 'B',
    (3,3) : 'C',
    (2,4) : 'D'
}
    
def new_loc((x, y), d):
    print repr(d)
    if d == 'U': nl = (x, y-1)
    elif d == 'D': nl = (x, y+1)
    elif d == 'L': nl = (x-1, y)
    elif d == 'R': nl = (x+1, y)
    if nl not in keys: return (x,y)
    return nl


cur = (0,2)
code = []

for line in sys.stdin:
    for c in line.strip():
        cur = new_loc(cur, c)
    code.append(keys[cur])
print ''.join(code)
            

