import sys
from collections import defaultdict, Counter

messages = [line.strip() for line in sys.stdin if line]
cols = zip(*messages)

print cols
msg = ''.join([Counter(c).most_common()[-1][0] for c in cols])
print msg
