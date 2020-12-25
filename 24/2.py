import sys

def main(in_string):
    tile_strings = in_string.split('\n')
    tiles = []
    ops = {'nw':'se','ne':'sw','e':'w','w':'e','sw':'ne','se':'nw'}
    for t in tile_strings:
        current = []
        tmp = t
        while len(tmp) > 0:
            if tmp[0] == 's' or tmp[0] == 'n':
                current.append(tmp[0]+tmp[1])
                if len(tmp) > 2:
                    tmp = tmp[2:]
                else:
                    tmp = []
            else:
                current.append(tmp[0])
                if len(tmp) > 1:
                    tmp = tmp[1:]
                else:
                    tmp = []
        tiles.append(current)

    end_points = [end_point(p) for p in tiles]
    colours = dict()
    for e in end_points:
        if not e in colours.keys():
            colours[e] = 'black'
        else:
            if colours[e] == 'black':
                colours[e] = 'white'
            else:
                colours[e] = 'black'

    black_tiles = []
    for k,v in colours.items():
        if v == 'black':
            black_tiles.append(k)

    for i in range(100):
        black_tiles = calc_tiles(black_tiles)

    print(len(black_tiles))

def calc_tiles(black_tiles):
    new_black = []
    tiles = dict()
    for b in black_tiles:
        if not b in tiles.keys():
            tiles[b] = 0
        ns = get_neighbours(b)
        for n in ns:
            if not n in tiles.keys():
                tiles[n] = 1
            else:
                tiles[n] += 1

    for t in tiles.keys():
        if t in black_tiles:
            if tiles[t] > 0 and tiles[t] <= 2:
                new_black.append(t)
        else:
            if tiles[t] == 2:
                new_black.append(t)
    return new_black



def get_neighbours(tile):
    adds_even = [(-1,1),(0,1),(-1,0),(1,0),(-1,-1),(0,-1)]
    adds_odd = [(0,1),(1,1),(-1,0),(1,0),(0,-1),(1,-1)]
    if tile[1]%2 == 0:
        adds = adds_even
    else:
        adds = adds_odd

    return [(tile[0] + a[0],tile[1] + a[1]) for a in adds]


def end_point(path):
    adds_even = {'nw':(-1,1),'ne':(0,1),'w':(-1,0),'e':(1,0),'sw':(-1,-1),'se':(0,-1)}
    adds_odd = {'nw':(0,1),'ne':(1,1),'w':(-1,0),'e':(1,0),'sw':(0,-1),'se':(1,-1)}
    current = (0,0)
    for p in path:
        if current[1] % 2 == 0:
            adds = adds_even
        else:
            adds = adds_odd
        current = (current[0] + adds[p][0], current[1] + adds[p][1])
    return current

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
