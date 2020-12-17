import sys
import itertools
import copy

def print_nd(state,n):
    print()
    for k in sorted(state.keys()):
        print('Dims =',k)
        grid = state[k]
        for row in grid:
            print(''.join(row))

        print()
    print('------------------')
    

def main(in_string):
    zero = list(map(list,in_string.split('\n')))
    nd = 4
    # minus 2 as our input is always 2d
    state = dict()
    zero_key = ''
    dmin = 0
    dmax = 0

    for i in range(nd-2):
        if i == nd-3:
            zero_key += '0'
        else:
            zero_key += '0,'
    state[zero_key] = zero

    print('------------------')
    print_nd(state,nd)
    
    for i in range(6):
        # expand existing
        for k in state.keys():
            new_col_no = len(state[k][0])+2
            new_2d = [['.' for c in range(new_col_no)]]
            for row in state[k]:
                new_row = ['.'] + row + ['.']
                new_2d.append(new_row)
            new_2d.append(['.' for c in range(new_col_no)])
            state[k] = new_2d


        # add new
        size = (len(state[list(state.keys())[0]]),len(state[list(state.keys())[0]][0]))
        empty_grid = [['.' for c in range(size[0])] for r in range(size[1])]

        dmin -= 1
        dmax += 1
        combs = list(itertools.product(list(range(dmin,dmax+1)),repeat=nd-2))
        for c in combs:
            new_key = ','.join(list(map(str,c)))
            if not new_key in state:
                state[new_key] = copy.deepcopy(empty_grid)

        # actually do game of life shit
        new_state = dict()
        for k in state.keys():
            new_grid = []
            grid = state[k]
            for y,row in enumerate(grid):
                new_row = []
                for x,entry in enumerate(row):
                    ns = get_active_neighbours(x,y,k,state)
                    if entry == '#':
                        if ns == 2 or ns == 3:
                            new_entry = '#'
                        else:
                            new_entry = '.'
                    else:
                        if ns == 3:
                            new_entry = '#'
                        else:
                            new_entry = '.'
                    new_row.append(new_entry)
                new_grid.append(new_row)
            new_state[k] = new_grid

        state = new_state

        print_nd(state,nd)

    count = 0
    for k in state.keys():
        grid = state[k]
        for row in grid:
            for entry in row:
                if entry == '#':
                    count += 1

    print('Active:',count)

def get_active_neighbours(x,y,k,state):
    ns = 0
    extra_ds = list(map(int,k.split(',')))
    all_ds = [[x-1,x,x+1] for x in extra_ds]
    combs = list(itertools.product(*all_ds))
    for c in combs:
        tmp_key = ','.join(list(map(str,c)))
        if tmp_key in state.keys():
            tmp_grid = state[tmp_key]
            for dy in range(-1,2):
                for dx in range(-1,2):
                    if not (tmp_key == k and dx == 0 and dy == 0):
                        if y+dy >= 0 and y+dy < len(tmp_grid) and x+dx >= 0 and x+dx < len(tmp_grid[0]):
                            if tmp_grid[y+dy][x+dx] == '#':
                                ns += 1

    return ns

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
