
import sys

def main(in_string):
    grid = in_string.split('\n')
    width = len(grid[0])
    height = len(grid)
    right = 3
    down = 1
    ch = 0
    cw = 0
    trees = 0
    while ch < height:
        if grid[ch][cw] == '#':
            trees += 1
        ch += down
        cw += right
        cw = cw % width
    print(trees)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
