import sys

with open('input','r') as f:
    lines = f.readlines()

nums = [int(l) for l in lines]

for idx, n1 in enumerate(nums):
    for idy, n2 in enumerate(nums):
        for idz, n3 in enumerate(nums):
            if not idx == idy and not idx == idz and not idy == idx:
                if n1 + n2 + n3 == 2020:
                    print(n1*n2*n3)
                    sys.exit(0)
