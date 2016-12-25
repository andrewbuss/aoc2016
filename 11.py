import sys
from collections import defaultdict, Counter

lines = [line.strip().split() for line in sys.stdin if line]

pc = 0
regs = dict(zip('abcd', [0]*4))

def op(r):
    if r not in regs: return int(r)
    return regs[r]

while pc < len(lines):
    instr = lines[pc]
    print pc, instr
    if instr[0] == 'jnz' and op(instr[1]) != 0:
        pc += op(instr[2])  - 1
    elif instr[0] == 'inc':
        regs[instr[1]] += 1
    elif instr[0] == 'dec':
        regs[instr[1]] -= 1
    elif instr[0] == 'cpy':
        regs[instr[2]] = op(instr[2])
    pc += 1

print regs['a']
