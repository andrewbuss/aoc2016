import sys

rs = []
for line in sys.stdin:
    a, b = map(int, line.strip().split('-'))
    rs.append((a,b))

rs.sort()

n = 0
ubt = 0
cap = 4294967296
rs.append((cap,cap))
while rs and n < cap:
    if n < rs[0][0]:
        ubt += rs[0][0] - n
    n = max(n, rs[0][1] + 1)
    rs.pop(0)

print n, ubt
