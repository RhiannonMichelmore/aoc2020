import sys

def main(in_string):
    nums = list(map(int,in_string.split(',')))
    seen = dict()
    last = nums[-1]
    for idx,n in enumerate(nums[:-1]):
        seen[n] = idx+1

    counter = len(nums)+1
    while True:
        if not last in seen.keys():
            seen[last] = counter-1
            last = 0
        else:
            new_last = counter-1-seen[last]
            seen[last] = counter-1
            last = new_last


        if counter == 2020:
            print(last)
            break
        counter += 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
