import networkx as nx
import sys

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
                weight = words[0]
                dest_node = ''.join(words[1:3])
                G.add_edge(node,dest_node,weight = weight)

    target = 'shinygold'
    ancestors = nx.ancestors(G,target)
    print(len(ancestors))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
