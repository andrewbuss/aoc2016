import sys
from collections import defaultdict, Counter

lines = [line.strip().split() for line in sys.stdin if line]

pc = 0
regs = dict(zip('abcd', [0]*4))
regs['a'] = 12

def op(r):
    if r not in regs: return int(r)
    return regs[r]

while pc < len(lines):
    instr = lines[pc]
    print pc, instr, regs
    if (pc < len(lines) - 5 and
        lines[pc+5] == ['jnz', 'd', '-5'] and
        lines[pc+4] == ['dec', 'd'] and
        lines[pc+3] == ['jnz', 'c', '-2'] and
        lines[pc+2] == ['dec', 'c'] and
        lines[pc+1] == ['inc', 'a'] and
        lines[pc] == ['cpy', 'b', 'c']):

        regs['a'] += regs["b"] * regs['d']
        regs["c"] = 0
        regs["d"] = 0
        pc = pc + 5
    if instr[0] == 'jnz' and op(instr[1]) != 0:
        pc += op(instr[2])  - 1
    elif instr[0] == 'inc':
        regs[instr[1]] += 1
    elif instr[0] == 'dec':
        regs[instr[1]] -= 1
    elif instr[0] == 'cpy':
        regs[instr[2]] = op(instr[1])
    elif instr[0] == 'tgl':
        npc = pc + op(instr[1])
        if 0 <= npc < len(lines):
            if lines[npc][0] == 'inc':
                lines[npc][0] = 'dec'
            elif lines[npc][0] == 'dec':
                lines[npc][0] = 'inc'
            elif lines[npc][0] == 'cpy':
                lines[npc][0] = 'jnz'
            elif lines[npc][0] == 'jnz':
                lines[npc][0] = 'cpy'
            elif lines[npc][0] == 'tgl':
                lines[npc][0] = 'inc'
            else:
                assert False

    pc += 1

print regs['a']
