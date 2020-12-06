import numpy as np
import sys

def main(in_string):
    groups = in_string.split('\n\n')
    g_counts = []
    for g in groups:
        indivs = [set(i) for i in g.split('\n')]
        base = indivs[0]
        for i in indivs[1:]:
            base = base.intersection(i)
        g_counts.append(len(base))
    print(sum(g_counts))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
