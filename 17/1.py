import sys

def main(in_string):
    z0 = list(map(list,in_string.split('\n')))

    state = [(0,z0)]
    print('------------------')
    print_3d(state)
    
    for i in range(6):
        # expand
        for idx,(n,z) in enumerate(state):
            new_col_no = len(z[0])+2
            new_z = [['.' for c in range(new_col_no)]]
            for r in z:
                new_r = ['.'] + r + ['.']
                new_z.append(new_r)
            new_z.append(['.' for c in range(new_col_no)])
            state[idx] = (n,new_z)


        # add new z's
        low_z = state[0][0]
        high_z = state[-1][0]
        # size = (rows,cols)
        size = (len(state[0][1]),len(state[0][1][0]))
        new_low = low_z-1
        new_high = high_z+1
        new_low_grid = [['.' for c in range(size[1])] for r in range(size[0])]
        new_high_grid = [['.' for c in range(size[1])] for r in range(size[0])]
        state.insert(0,(new_low,new_low_grid))
        state.append((new_high,new_high_grid))

        # actually do game of life shit
        new_state = []
        for (z,grid) in state:
            upper = get_neighbour(state,z,1)
            lower = get_neighbour(state,z,-1)
            new_grid = resolve(grid,upper,lower)
            new_state.append((z,new_grid))
        state = new_state
        print_3d(state)

    count = 0
    for (z,s) in state:
        for r in s:
            for e in r:
                if e == '#':
                    count += 1

    print('Active:',count)

def get_neighbour(state,z,diff):
    n = [v for v in state if v[0] == z + diff]
    if len(n) == 0:
        return None
    else:
        return n[0][1]

def resolve(grid,upper,lower):
    new_grid = []
    for y,row in enumerate(grid):
        new_row = []
        for x,entry in enumerate(row):
            ns = get_neighbours(x,y,grid,upper,lower)
            if entry == '.':
                if ns == 3:
                    new_entry = '#'
                else:
                    new_entry = '.'
            elif entry == '#':
                if ns == 2 or ns == 3:
                    new_entry = '#'
                else:
                    new_entry = '.'
            new_row.append(new_entry)
        new_grid.append(new_row)
    return new_grid

def get_neighbours(x,y,grid,upper,lower):
    ns = 0
    for z in range(-1,2):
        if z == -1:
            if lower == None:
                continue
            tmp = lower
        elif z == 0:
            tmp = grid
        elif z == 1:
            if upper == None:
                continue
            tmp = upper
        for yy in range(-1,2):
            for xx in range(-1,2):
                if not (yy == 0 and xx == 0 and z == 0):
                    if y+yy >= 0 and y+yy < len(tmp) and x+xx >= 0 and x+xx < len(tmp[0]):
                        if tmp[y+yy][x+xx] == '#':
                            ns += 1

    return ns


def print_3d(state):
    print()
    for (z,l) in state:
        print_2d(z,l)
    print('-----------------')

def print_2d(z,grid):
    print('z='+str(z))
    for row in grid:
        print(''.join(row))
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
