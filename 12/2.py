import numpy as np
import sys

def main(in_string):
    instrs = in_string.split('\n')
    heading = 1 # 0 = north, 1 = east, 2 = south, 3 = west
    x = 0 # positive x = east
    y = 0 # positve y = south

    
    w_x = 10
    w_y = -1

    for ins in instrs:
        letter = ins[0]
        param = int(ins[1:])
        if letter == 'N':
            w_y -= param
        elif letter == 'E':
            w_x += param
        elif letter == 'S':
            w_y += param
        elif letter == 'W':
            w_x -= param
        elif letter == 'R':
            param = param%360
            if param == 90:
                tmp = w_x
                w_x = -w_y
                w_y = tmp
            elif param == 180:
                w_x = -w_x
                w_y = -w_y
            elif param == 270:
                tmp = w_x
                w_x = w_y
                w_y = -tmp
        elif letter == 'L':
            param = param%360
            if param == 90:
                tmp = w_x
                w_x = w_y
                w_y = -tmp
            elif param == 180:
                w_x = -w_x
                w_y = -w_y
            elif param == 270:
                tmp = w_x
                w_x = -w_y
                w_y = tmp
        elif letter == 'F':
            x_forward = w_x*param
            y_forward = w_y*param
            x += x_forward
            y += y_forward

    print(abs(x)+abs(y))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
