import sys

def main(in_string):
    lines = in_string.split('\n')
    mask = ''
    m1s = ''
    m0s = ''
    mem = dict()
    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' ')[2]
            m1s = [idx for idx,x in enumerate(mask) if x == '1']
            m0s = [idx for idx,x in enumerate(mask) if x == '0']
        else:
            index = line.split(' ')[0].split('[')[1][:-1]
            val = "{0:b}".format(int(line.split(' ')[2]))
            if len(val) < len(mask):
                val = '0'*(len(mask)-len(val)) + val

            val = list(val)
            for m1 in m1s:
                val[m1] = '1'

            for m0 in m0s:
                val[m0] = '0'

            val = ''.join(val)
            mem[index] = val

    acc = 0
    for k in mem.keys():
        acc += int(mem[k],2)

    print(acc)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
