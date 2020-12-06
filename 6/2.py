import numpy as np
import sys

def main(in_string):
    print(sum([len(set.intersection(*list(map(set,g.split('\n'))))) for g in in_string.split('\n\n')]))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
