def solve(n):
    l = [True] * n
    i = 0
    for _ in range(n-1):
        while not l[i%n]: i += 1
        i += 1
        while not l[i%n]: i += 1
        l[i%n] = False
        i += 1
        #print i, l
    return l.index(True) + 1

def solve2(n):
    if n == 1: return 0
    if n == 2: return 0
    x = (n)/2
    r = solve2(n-1)
    print n, x, r
    if r + 1 >= x:
        return (r+2)%n
    else:
        return (r+1)%n




print map(solve2, range(1,10))
print solve2(3001330) 
