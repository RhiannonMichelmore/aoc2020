
import sys

def main(in_string):
    instrs = in_string.split('\n')
    acc = 0
    pc = 0
    visited = []
    while pc < len(instrs):
        if pc in visited:
            print('loop')
            print('acc:',acc)
            sys.exit(0)
        visited.append(pc)
        current = instrs[pc]
        instruct = current.split(' ')[0]
        arg = int(current.split(' ')[1])
        if instruct == 'nop':
            pc += 1
        elif instruct == 'acc':
            pc += 1
            acc += arg
        elif instruct == 'jmp':
            pc += arg


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
