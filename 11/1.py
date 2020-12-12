import copy
import sys

def occupied_neighbours(rn,cn,grid):
    occ = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if (not i == 0 or not j == 0) and (rn+i >= 0 and rn+i < len(grid) and cn+j >= 0 and cn+j < len(grid[0])):
                if grid[rn+i][cn+j] == '#':
                    occ += 1
    return occ

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col,end='')
        print()
    print()

def main(in_string):
    grid = in_string.split('\n')
    print_grid(grid)

    mods = True
    while mods == True:
        new_grid = []
        mods = False
        for r,row in enumerate(grid):
            new_grid.append([])
            for c,col in enumerate(row):
                if col == 'L':
                    if occupied_neighbours(r,c,grid) == 0:
                        new_grid[-1].append('#')
                        mods = True
                    else:
                        new_grid[-1].append('L')
                elif col == '.':
                    new_grid[-1].append('.')
                elif col == '#':
                    if occupied_neighbours(r,c,grid) >= 4:
                        new_grid[-1].append('L')
                        mods = True
                    else:
                        new_grid[-1].append('#')
        grid = new_grid
        #print_grid(grid)

    print(sum([x.count('#') for x in grid]))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
