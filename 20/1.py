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
    total = 1
    for c in corners:
        total *= c

    print(total)

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
