
import sys

def main(in_string):
    jolts = [int(x) for x in in_string.split('\n')]
    rating = max(jolts)+3
    jolts = sorted(jolts)
    jolts = [0] + jolts + [rating]
    diffs = [jolts[i+1]-jolts[i] for i in range(len(jolts)-1)]
    zeros = diffs.count(0)
    ones = diffs.count(1)
    threes = diffs.count(3)
    twos = diffs.count(2)
    print("zeros",zeros,"ones:",ones,"twos:",twos,"threes:",threes,"prod:",ones*threes)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
