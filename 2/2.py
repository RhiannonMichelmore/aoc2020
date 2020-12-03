
import sys

def main(in_string):
    lines = in_string.split('\n')
    valid = 0
    for line in lines:
        spl = line.split(' ')
        rule = spl[0]
        pos1 = int(rule.split('-')[0]) - 1
        pos2 = int(rule.split('-')[1]) - 1
        letter = spl[1][0]
        password = spl[2]
        if (password[pos1] == letter and not password[pos2] == letter) or (not password[pos1] == letter and password[pos2] == letter):
            valid += 1

    print(valid)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
