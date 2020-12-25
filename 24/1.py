import sys
import networkx as nx

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

    '''
    G = nx.DiGraph()
    G.add_node('root',colour='white',path=[])
    node_counter = 1
    for t in tiles:
        current = 'root'
        print('current',current)
        for direction in t:
            out_edges = G.out_edges(current,data='direction')
            out_edges_list = [x for x in out_edges]
            out_dirs = [x[2] for x in out_edges]
            if direction in out_dirs:
                idx = out_dirs.index(direction)
                terminal = out_edges_list[idx][1]
                current = terminal
#                print('moving to existing id',current)
            else:
                existing_path = G.nodes[current]['path']
                new_path = existing_path + [direction]
                same = get_same(G,new_path)
                if same == None:
#                    print('adding new node')
                    G.add_node(node_counter,colour='white',path=new_path)
                    new = node_counter
                    G.add_edge(current,new,direction=direction)
                    G.add_edge(new,current,direction = ops[direction])
#                    print('new id',new)
                    current = new
                    node_counter += 1
                else:
                    print('rejoining existing node')
                    current = same
        end = G.nodes[current]['colour']
#        print(end)
        if end == 'white':
            G.nodes[current]['colour'] = 'black'
        else:
            G.nodes[current]['colour'] = 'white'

    black_nodes = [x for x,y in G.nodes(data=True) if y['colour'] == 'black']
    print(len(black_nodes))

    '''
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

    count = 0
    for k,v in colours.items():
        if v == 'black':
            count += 1

    print(count)


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

def get_same(G,path):
    # if they have the same directions in their path (in any order), the end node is the same
    same = None
    for node in G.nodes():
        if end_point(path) == end_point(G.nodes[node]['path']):
            same = node
            break
    return same


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
