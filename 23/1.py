import sys

def main(in_string):
    ring = list(map(int,list(in_string)))

    ring = [r-1 for r in ring]
    length = len(ring)

    print([r+1 for r in ring])
    print()
    current = ring[0]
    for i in range(100):
        three = []
        current_idx = ring.index(current)
        for j in range(3):
            to_pop = (current_idx+1)%len(ring)
            if to_pop < current_idx:
                current_idx -= 1
            three.append(ring.pop(to_pop))

        invalid = True
        c = 1
        while invalid:
            dest = (current-c)%9
            if not dest in three:
                invalid = False
            else:
                c += 1
        idx = ring.index(dest)
        if not idx == len(ring)-1:
            ring = ring[:idx+1] + three + ring[idx+1:]
        else:
            ring = ring + three

        current_idx = ring.index(current)
        current_idx = (current_idx+1)%9
        current = ring[current_idx]

    print_ring = [r+1 for r in ring]
    one_idx = print_ring.index(1)
    if one_idx < len(print_ring)-1:
        rearrange = print_ring[one_idx+1:] + print_ring[:one_idx]
    else:
        rearrange = print_ring[:-1]

    print(''.join(list(map(str,rearrange))))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
