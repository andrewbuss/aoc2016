import sys
from collections import defaultdict, Counter

lines = [line.strip() for line in sys.stdin if line]
pixels = [[0 for x in range(50)] for y in range(6)]

for line in lines:
    print line
    if 'rect' in line:
        dx, dy = map(int, line.split(' ')[1].split('x'))
        for x in range(dx):
            for y in range(dy):
                pixels[y][x] = 1
        print x,y
    else:
        line = line.split()
        if 'row' in line:
            rownum = int(line[2].split('=')[1])
            offset = int(line[4])
            print rownum, offset
            pixels[rownum] = pixels[rownum][-offset:] + pixels[rownum][:50-offset]
        elif 'column' in line:
            colnum = int(line[2].split('=')[1])
            offset = int(line[4])
            pixels = zip(*pixels)
            print colnum, offset
            pixels[colnum] = pixels[colnum][-offset:] + pixels[colnum][:6-offset]
            pixels = map(list, zip(*pixels))
    for row in pixels: print ''.join(map(lambda c: '#' if c else ' ',row))


print sum(map(sum, pixels))
