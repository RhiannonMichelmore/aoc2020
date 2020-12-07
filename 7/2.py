import networkx as nx
from networkx.algorithms.simple_paths import all_simple_paths
import sys
import numpy as np

def main(in_string):
    G = nx.DiGraph()
    for rule in in_string.split('\n'):
        node = ''.join(rule.split(' ')[:2])
        for child_string in ' '.join(rule.split(' ')[4:]).split(','):
            child_string = child_string.strip()
            words = child_string.split(' ')
            if words[0] == 'no':
                G.add_node(node)
            else:
                weight = int(words[0])
                dest_node = ''.join(words[1:3])
                if G.has_edge(node,dest_node):
                    G[node][dest_node]['weight'] += weight
                else:
                    G.add_edge(node,dest_node,weight = weight)

    target = 'shinygold'
    total = get_cost(G,target)
    # ignore shinygold
    total -= 1
    print(total)

def get_cost(G,root):
    total = 1
    for succ in G.successors(root):
        weight = G[root][succ]['weight']
        c = get_cost(G,succ)
        total += (c*weight)
    return total


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
