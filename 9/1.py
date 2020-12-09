import sys

def is_sum_of(number,n_list):
    for i, n1 in enumerate(n_list):
        for j, n2 in enumerate(n_list):
            if not i == j:
                if n1 + n2 == number:
                    return True
    return False

def main(in_string):
    whole_list = [int(x) for x in in_string.split('\n')]
    p_size = 5
    rolling = whole_list[:p_size]
    rest = whole_list[p_size:]

    for r in rest:
        if not is_sum_of(r,rolling):
            print(r)
            break
        else:
            rolling = rolling[1:] + [r]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
