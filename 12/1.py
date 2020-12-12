
import sys

def main(in_string):
    instrs = in_string.split('\n')
    heading = 1 # 0 = north, 1 = east, 2 = south, 3 = west
    x = 0 # positive x = east
    y = 0 # positve y = south

    for ins in instrs:
        letter = ins[0]
        param = int(ins[1:])
        if letter == 'N':
            y -= param
        elif letter == 'E':
            x += param
        elif letter == 'S':
            y += param
        elif letter == 'W':
            x -= param
        elif letter == 'R':
            heading = (heading + (param/90)) % 4
        elif letter == 'L':
            heading = (heading - (param/90)) % 4
        elif letter == 'F':
            if heading == 0:
                y -= param
            elif heading == 1:
                x += param
            elif heading == 2:
                y += param
            elif heading == 3:
                x -= param

    print(abs(x)+abs(y))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
