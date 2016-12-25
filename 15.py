import hashlib

def do_hash(n):
    return hashlib.md5('abc'+str(n)).hexdigest()

for i in range(100):
    print do_hash(i)
