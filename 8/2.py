
import sys

def run_program(instrs,idx_to_flip):
    acc = 0
    pc = 0
    visited = []
    looped = False
    while pc < len(instrs):
        if pc in visited:
            looped = True
            break
        visited.append(pc)
        current = instrs[pc]
        instruct = current.split(' ')[0]
        if pc == idx_to_flip:
            instruct = 'nop' if instruct == 'jmp' else 'jmp'
        arg = int(current.split(' ')[1])
        if instruct == 'nop':
            pc += 1
        elif instruct == 'acc':
            pc += 1
            acc += arg
        elif instruct == 'jmp':
            pc += arg
    if looped == False:
        print('no loop when flip instr',idx_to_flip,instrs[idx_to_flip])
        print('acc:',acc)
    return looped

def main(in_string):
    instrs = in_string.split('\n')
    # idx, arg
    jmps = [(a,int(b.split(' ')[1])) for (a,b) in zip(list(range(len(instrs))),instrs) if b.startswith('jmp')]
    nops = [(a,int(b.split(' ')[1])) for (a,b) in zip(list(range(len(instrs))),instrs) if b.startswith('nop')]
    for (idx,old_arg) in jmps:
        looped = run_program(instrs,idx)
        if looped == False:
            break


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
