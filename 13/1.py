import sys

def main(in_string):
    early = int(in_string.split('\n')[0])
    buses = in_string.split('\n')[1]
    ids = [int(x) for x in buses.split(',') if not x == 'x']
    closest = 0
    cn = 0
    for i in ids:
        n = int(early/i)*i
        if n < early:
            n += i
        if abs(early - n) < abs(early - cn):
            cn = n
            closest = i

    print(cn, closest, abs(early-cn))
    print(closest*abs(early-cn))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
