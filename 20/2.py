import sys

def main(in_string):
    tile_strings = in_string.split('\n\n')
    tiles = dict()
    for ts in tile_strings:
        key_str = ts.split('\n')[0]
        key = int(key_str.split(' ')[1][:-1])
        tile = list(map(list,ts.split('\n')[1:]))
        tiles[key] = tile

    edges = []
    edge_ids = []
    for t in tiles.keys():
        tile = tiles[t]
        top = tile[0]
        bottom = tile[-1]
        left = [x[0] for x in tile]
        right = [x[-1] for x in tile]
        edges += [top,bottom,left,right]
        edge_ids.append(t)

    borders = []
    for idx,e in enumerate(edges):
        edge_id_idx = int(idx/4)
        edge_id = edge_ids[edge_id_idx]
        c = edges.count(e) + edges.count(e[::-1])
        if c == 1:
            borders.append(edge_id)


    new_borders = []
    corners = []
    for b in borders:
        if borders.count(b) > 1:
            if b not in corners:
                corners.append(b)
        else:
            new_borders.append(b)

    borders = new_borders

    # assemble outer ring
    side = int(len(tiles.keys())**0.5)
    # just pick a starting corner
    bottom_left = tiles[corners[0]]
    grid = dict()
    for i in range(side):
        grid[i] = dict()

    # figure out how to rotate bottom left so it has unique sides on bottom and left
    bottom_left = transform_match(bottom_left,None,'unique','unique',None,edges)
    # grid[y][x]
    grid[0][0] = bottom_left
    # get left side
    all_tiles = list(tiles.keys())
    used_tiles = [corners[0]]
    for y in range(side):
        # moving along the bottom and up layers
        for x in range(side):
            if not (x == 0 and y == 0):
                # take from corners
                left_match = None
                right_match = None
                top_match = None
                bottom_match = None
                border = False
                corner = False
                if y == 0 and x == side-1:
                    # it is bottom right corner, bottom and right and unique, left matches right side of prev
                    left_match = [a[-1] for a in grid[y][x-1]]
                    corner = True
                elif y == side-1 and x == 0:
                    # it is top left corner, top and left unique, bottom matches top of prev
                    bottom_match = grid[y-1][x][0]
                    corner = True
                elif y == side-1 and x == side-1:
                    # it is top right corner, top and right unique, left matched prev right, bottom matches under top
                    bottom_match = grid[y-1][x][0]
                    left_match = [a[-1] for a in grid[y][x-1]]
                    corner = True
                elif x == 0:
                    # it is left side, bottom matches top of under, left is unique
                    border = True
                    bottom_match = grid[y-1][x][0]
                elif x == side-1:
                    # it is right side, bottom matches top of under, left matches right of prev, right is unique
                    border = True
                    bottom_match = grid[y-1][x][0]
                    left_match = [a[-1] for a in grid[y][x-1]]
                elif y == 0:
                    # it is bottom side, left matches right of prev, bottom is unique
                    border = True
                    left_match = [a[-1] for a in grid[y][x-1]]
                elif y == side-1:
                    # it is top side, top is unique, left matches right of prev, bottom matched top of under
                    border = True
                    left_match = [a[-1] for a in grid[y][x-1]]
                    bottom_match = grid[y-1][x][0]
                else:
                    # its a central piece, match left and bottom
                    left_match = [a[-1] for a in grid[y][x-1]]
                    bottom_match = grid[y-1][x][0]

                to_remove = -1
                for idx,c in enumerate(all_tiles):
                    if not c in used_tiles:
                        tmp_tile = tiles[c].copy()
                        if corner == True:
                            if not c in corners:
                                continue
                        elif border == True:
                            if not c in borders:
                                continue
                        tmp_tile = transform_match(tmp_tile,top_match,bottom_match,left_match,right_match,edges)
                        if not tmp_tile == None:
                            to_remove = idx
                            grid[y][x] = tmp_tile
                            used_tiles.append(c)
                            break

    print_grid(grid,side,len(tiles[list(tiles.keys())[0]][0]))

    mega_grid = []
    for y in range(side):
        tiles_to_join = []
        for x in range(side):
            tmp = grid[side-y-1][x]
            tmp = [a[1:-1] for a in tmp][1:-1]
            tiles_to_join.append(tmp)
        for i in range(len(tiles_to_join[0])):
            mega_row = []
            for j in range(len(tiles_to_join)):
                mega_row += tiles_to_join[j][i]
            mega_grid.append(mega_row)
    print()
    pp(mega_grid)

    rotation = 0
    while rotation < 4:
        sea_monsters = find_seamonsters(mega_grid)
        if not sea_monsters == None:
            break
        sea_monsters = find_seamonsters(mega_grid[::-1])
        if not sea_monsters == None:
            mega_grid = mega_grid[::-1]
            break
        sea_monsters = find_seamonsters([a[::-1] for a in mega_grid])
        if not sea_monsters == None:
            mega_grid = [a[::-1] for a in mega_grid]
            break
        sea_monsters = find_seamonsters([a[::-1] for a in mega_grid][::-1])
        if not sea_monsters == None:
            mega_grid = [a[::-1] for a in mega_grid][::-1]
            break
        mega_grid = list(map(list,zip(*mega_grid[::-1])))
        rotation += 1

    hash_count = sum([a.count('#') for a in mega_grid])
    # sea monsters have 15 hashes and dont overlap
    total = hash_count - (len(sea_monsters)*15)
    print(total)

def find_seamonsters(grid):
    # positive y is downward
    # offset from position top left = 0
    monster = [(18, 0), (0, 1), (5, 1), (6, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1), (1, 2), (4, 2), (7, 2), (10, 2), (13, 2), (16, 2)]
    coords = None
    for y in range(len(grid)-2):
        for x in range(len(grid)-18):
            found = True
            for (xx,yy) in monster:
                if not grid[y+yy][x+xx] == '#':
                    found = False
                    break
            if found == True:
                if coords == None:
                    coords = [(x,y)]
                else:
                    coords.append((x,y))
    return coords

def print_grid(grid,size,gsize):
    for y in range(size):
        tiles_to_print = []
        for x in range(size):
            if not x in grid[size-y-1]:
                tiles_to_print.append([['.' for g in range(gsize)] for g in range(gsize)])
            else:
                tiles_to_print.append(grid[size-y-1][x])
        for i in range(gsize):
            mega_row = ' '.join([''.join(t[i]) for t in tiles_to_print])
            print(mega_row)
        print()

def transform_match(tile, top_match,bottom_match,left_match,right_match,edges):
    # try:  1. match as is
    #       3. flip x, match
    #       4. flip y, match
    #       5. flip xy, match
    # rotate once and try again until rotated 3 times total
    rotated = 0
    while rotated < 4:
        if match(tile,top_match,bottom_match,left_match,right_match,edges):
            return tile

        x_flipped = [x[::-1] for x in tile]
        if match(x_flipped,top_match,bottom_match,left_match,right_match,edges):
            return x_flipped

        y_flipped = tile[::-1]
        if match(y_flipped,top_match,bottom_match,left_match,right_match,edges):
            return y_flipped
        
        xy_flipped = [x[::-1] for x in tile][::-1]
        if match(xy_flipped,top_match,bottom_match,left_match,right_match,edges):
            return xy_flipped

        # rotate 90 degrees
        tile = list(map(list,zip(*tile[::-1])))
        rotated += 1

    return None


def match(tile,top_match,bottom_match,left_match,right_match,edges):
    top = tile[0]
    bottom = tile[-1]
    left = [x[0] for x in tile]
    right = [x[-1] for x in tile]

    if not top_match == None:
        if top_match == 'unique':
            if edges.count(top) + edges.count(top[::-1]) > 1:
                return False
        else:
            if not top == top_match:
                return False

    if not bottom_match == None:
        if bottom_match == 'unique':
            if edges.count(bottom) + edges.count(bottom[::-1]) > 1:
                return False
        else:
            if not bottom == bottom_match:
                return False

    if not left_match == None:
        if left_match == 'unique':
            if edges.count(left) + edges.count(left[::-1]) > 1:
                return False
        else:
            if not left == left_match:
                return False

    if not right_match == None:
        if right_match == 'unique':
            if edges.count(right) + edges.count(right[::-1]) > 1:
                return False
        else:
            if not right == right_match:
                return False
    return True


def pp(tile):
    for line in tile:
        print(''.join(line))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
