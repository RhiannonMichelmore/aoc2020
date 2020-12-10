import sys
import math
import numpy as np

def nCr(n,r):
    return math.factorial(n) / math.factorial(n-r)  

def main(in_string):
    jolts = [int(x) for x in in_string.split('\n')]
    rating = max(jolts)+3
    jolts = sorted(jolts)
    jolts = [0] + jolts + [rating]

    orig_len = len(jolts)
    print('orig len:',orig_len)
    print('rating:',rating)

    combs = []
    one_set = []
    for i in range(len(jolts)):
        if len(one_set) > 0:
            if jolts[i]-one_set[-1] == 1:
                one_set.append(jolts[i])
            else:
                # have to keep first and last in each set as no 2 gaps
                # manually calculated lol, stretch of 1 diffs is at max 5 long only
                if len(one_set) <= 2:
                    combs.append(1)
                elif len(one_set) == 3:
                    combs.append(2)
                elif len(one_set) == 4:
                    combs.append(4)
                elif len(one_set) == 5:
                    combs.append(7)

                one_set = [jolts[i]]
        else:
            one_set.append(jolts[i])

    print(np.prod(combs))



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
