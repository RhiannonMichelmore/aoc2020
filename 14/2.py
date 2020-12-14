import sys
import itertools

def main(in_string):
    lines = in_string.split('\n')
    mask = ''
    m1s = ''
    mXs = ''
    mem = dict()
    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' ')[2]
            m1s = [idx for idx,x in enumerate(mask) if x == '1']
            mXs = [idx for idx,x in enumerate(mask) if x == 'X']
        else:
            index = "{0:b}".format(int(line.split(' ')[0].split('[')[1][:-1]))
            val = int(line.split(' ')[2])
            if len(index) < len(mask):
                index = '0'*(len(mask)-len(index)) + index

            index = list(index)
            for m1 in m1s:
                index[m1] = '1'

            combs = list(map(list, itertools.product([0,1],repeat=len(mXs))))
            for c in combs:
                tmp_index = index.copy()
                for idx,i in enumerate(c):
                    tmp_index[mXs[idx]] = str(i)
                dec = int(''.join(tmp_index),2)
                mem[dec] = val



    acc = 0
    for k in mem.keys():
        acc += mem[k]

    print(acc)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
