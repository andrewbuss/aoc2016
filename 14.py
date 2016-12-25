import hashlib

hs = {}

def stretch(x):
    for _ in range(2017):
        x = hashlib.md5(x).hexdigest()
    return x
    

def do_hash(n):
    if n not in hs:
        #hs[n] = stretch('abc%d'%n)
        hs[n] = stretch('ihaygndm%d'%n)
        
    return hs[n]


possible_fives = [c*5 for c in '0123456789abcdef']
possible_threes = [c*3 for c in '0123456789abcdef']

def fives(s):
    for f in possible_fives:
        if f in s:
            yield f

n = 0
keys = set()
for i in range(300000):
    if len(keys) == 64: break
    h = do_hash(i)
    for j in range(30):
        if h[j] == h[j+1] == h[j+2]:
            for d in range(1000):
                h2 = do_hash(i+d+1)
                if h[j]*5 in h2:
                    print i, i+d+1, h, h2
                    keys.add(i)
            break

for i, k in enumerate(sorted(keys)):
    print i, k
