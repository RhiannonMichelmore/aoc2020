import numpy as np
import sys

def main(in_string):
    grid = in_string.split('\n')
    width = len(grid[0])
    height = len(grid)
    rights = [1,3,5,7,1]
    downs = [1,1,1,1,2]
    trees = []
    for (r,d) in zip(rights,downs):
        ch = 0
        cw = 0
        curr_trees = 0
        while ch < height:
            if grid[ch][cw] == '#':
                curr_trees += 1
            ch += d
            cw += r
            cw = cw % width
        trees.append(curr_trees)

    print(np.prod(trees))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
