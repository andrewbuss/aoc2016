inp = raw_input()

dirs = [(0,1), (-1,0),(0,-1),(1,0)]
dir = 0
loc = (0,0)
visited = set()
n = 0
twice_visited = []
for m in inp.split(', '):
    if m[0] == 'L':
        dir += 1
    else:
        dir -= 1
    dir %= 4
    dist = int(m[1:])
    for _ in range(dist):
        loc = tuple([l + d for l, d in zip(loc, dirs[dir])])
        if loc in visited:
            twice_visited.append((n, loc))
        visited.add(loc)
        n += 1

twice_visited.sort()
print twice_visited
print sum(map(abs, twice_visited[0][1]))
print "final dist", sum(map(abs, loc))
