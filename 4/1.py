
import sys

def main(in_string):
    pstrs = in_string.split('\n\n')
    passports = []
    valid_keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] # dont need cid
    valid = 0
    for p in pstrs:
        doc = dict()
        p = p.replace('\n',' ')
        entries = p.split(' ')
        for e in entries:
            key = e.split(':')[0]
            value = e.split(':')[1]
            doc[key] = value
        has_keys = [x for x in doc.keys() if not x == 'cid']
        if set(has_keys) == set(valid_keys):
            valid += 1

    print(valid)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
