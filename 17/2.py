import sys

def main(in_string):
    z0 = list(map(list,in_string.split('\n')))

    state = [[z0]]
    # state[w][z][y][x]

    print('------------------')
    print_4d(state)
    
    for i in range(6):
        # expand
        for w,grid_3d in enumerate(state):
            for z,grid_2d in enumerate(grid_3d):
                new_col_no = len(grid_2d[0])+2
                new_2d = [['.' for c in range(new_col_no)]]
                for r in grid_2d:
                    new_r = ['.'] + r + ['.']
                    new_2d.append(new_r)
                new_2d.append(['.' for c in range(new_col_no)])
                state[w][z] = new_2d

        

        size = (len(state[0][0]),len(state[0][0][0]))
        for w,grid_3d in enumerate(state):
            lg = [['.' for c in range(size[0])] for r in range(size[1])]
            hg = [['.' for c in range(size[0])] for r in range(size[1])]
            state[w].insert(0,lg)
            state[w].append(hg)

        z_size = len(state[0])
        lg = [[['.' for c in range(size[0])] for r in range(size[1])] for f in range(z_size)]
        hg = [[['.' for c in range(size[0])] for r in range(size[1])] for f in range(z_size)]
        state.insert(0,lg)
        state.append(hg)

        # actually do game of life shit
        new_state = []
        for w,grid_3d in enumerate(state):
            new_3d = []
            for z, grid_2d in enumerate(grid_3d):
                new_2d = []
                for y, row in enumerate(grid_2d):
                    new_row = []
                    for x,entry in enumerate(row):
                        ns = get_active_neighbours(x,y,z,w,state)
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
                    new_2d.append(new_row)
                new_3d.append(new_2d)
            new_state.append(new_3d)


        state = new_state
        print_4d(state)

    count = 0
    for g3 in state:
        for g2 in g3:
            for r in g2:
                for e in r:
                    if e == '#':
                        count += 1

    print('Active:',count)

def get_active_neighbours(x,y,z,w,state):
    ns = 0
    for dw in range(-1,2):
        for dz in range(-1,2):
            for dy in range(-1,2):
                for dx in range(-1,2):
                    if not (dw == 0 and dz == 0 and dy == 0 and dx == 0):
                        if in_limit(x+dx,y+dy,z+dz,w+dw,state):
                            if state[w+dw][z+dz][y+dy][x+dx] == '#':
                                ns += 1

    return ns

def in_limit(x,y,z,w,state):
    if w >= 0 and w < len(state) and z >= 0 and z < len(state[0]) and y >= 0 and y < len(state[0][0]) and x >= 0 and x < len(state[0][0][0]):
        return True
    else:
        return False

def print_4d(state):
    print()
    for w,grid_3d in enumerate(state):
        print_3d(w,grid_3d)
    print('-----------------')

def print_3d(w,grid_3d):
    for z,grid_2d in enumerate(grid_3d):
        print_2d(w,z,grid_2d)

def print_2d(w,z,grid):
    print('z='+str(z),'w='+str(w))
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
