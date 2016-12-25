import hashlib

did = 'uqwqemis'
#did = 'abc'
i = 0
p = list('????????')
while '?' in p:
    h = hashlib.md5(did + str(i)).hexdigest()
    loc = int(h[5],16)
    if h[:5] == '00000' and loc < 8:
        print h
        if p[loc] == '?':
            p[loc] = h[6]
            print p
    i += 1
print ''.join(p)
