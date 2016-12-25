def gen_square((x,y)):
    n = x*x + 3*x + 2*x*y + y + y*y
    n += 1352
    if bin(n).count('1') % 2 == 0:
        return False
    else:
        return True

board = [[gen_square((x,y)) for y in range(80)] for x in range(80)]

by_dist = [[(1, 1)]]
by_sq = {}

def show_board():
    for y in range(50):
        for x in range(50):
            if (x,y) == (31,39): print "XX",
            elif board[x][y]: print "##",
            elif (x,y) not in by_sq: print "  ",
            else: print "%2d" % by_sq[(x,y)],
        print

for d in range(1, 200):
    by_dist.append(set())
    for (x,y) in by_dist[d-1]:
        if (x,y) in by_sq: continue
        by_sq[(x, y)] = d - 1
        if x > 0 and (x-1, y) not in by_sq:
            by_dist[d].add((x-1, y))
        if y > 0 and (x, y-1) not in by_sq:
            by_dist[d].add((x, y-1))
        by_dist[d].add((x+1, y))
        by_dist[d].add((x, y+1))
    by_dist[d] = filter(lambda (x,y): not board[x][y] and (x,y) not in by_sq, by_dist[d])
    print d, by_dist[d]
    if (31, 39) in by_sq:
        break

show_board()
print sum(map(len, by_dist[:51]))
