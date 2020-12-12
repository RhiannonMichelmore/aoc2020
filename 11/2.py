import copy
import sys

def occupied_sighted(rn,cn,grid):
    occ = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if not (i==0 and j==0):
                not_ended = True
                tmp_r = rn + i
                tmp_c = cn + j
                while not_ended:
                    if in_grid(tmp_r,tmp_c,grid):
                        if grid[tmp_r][tmp_c] == '#':
                            occ += 1
                            not_ended = False
                        elif grid[tmp_r][tmp_c] == 'L':
                            not_ended = False
                        else:
                            tmp_r += i
                            tmp_c += j
                    else:
                        not_ended = False

    return occ

def in_grid(r,c,grid):
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col,end='')
        print()
    print()

def main(in_string):
    grid = in_string.split('\n')
    print_grid(grid)

    #print(occupied_sighted(4,3,grid))

    mods = True
    while mods:
        new_grid = []
        mods = False
        for r,row in enumerate(grid):
            new_grid.append([])
            for c,col in enumerate(row):
                if col == 'L':
                    if occupied_sighted(r,c,grid) == 0:
                        new_grid[-1].append('#')
                        mods = True
                    else:
                        new_grid[-1].append('L')
                elif col == '.':
                    new_grid[-1].append('.')
                elif col == '#':
                    if occupied_sighted(r,c,grid) >= 5:
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
