import sys
from collections import defaultdict, Counter

addresses = [line.strip() for line in sys.stdin if line]

def has_abba(a):
    for i in range(len(a) - 3):
        if a[i] == a[i+3] and a[i+1] == a[i+2] and a[i] != a[i+1]:
            return True
    return False

def abas(a):
    for i in range(len(a) - 2):
        if a[i] == a[i+2] and a[i] != a[i+1]:
            yield a[i:i+3]

invert_aba = lambda x: x[1] + x[0] + x[1]

def is_ssl(a):
    b = 0
    cur = ''
    in_brackets = []
    out_brackets = []
    for c in addr + '[':
        if c not in '[]':
            cur += c
        else:
            if b == 0:
                out_brackets.append(cur)
            else:
                in_brackets.append(cur)
            cur = ''
            if c == '[':
                b += 1
            elif c == ']':
                b -= 1
    print in_brackets
    print out_brackets
    #return any(map(has_abba, out_brackets)) and not any(map(has_abba, in_brackets))
    if set(x for seg in out_brackets for x in abas(seg)) & \
       set(invert_aba(x) for seg in in_brackets for x in abas(seg)):
        return True
    

    
n = 0
import re
for addr in addresses:
    print addr
    if is_ssl(addr): n += 1
print n
    
