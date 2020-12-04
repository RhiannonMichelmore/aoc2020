# 115 too high
import sys

def main(in_string):
    pstrs = in_string.split('\n\n')
    valid_keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] # dont need cid
    v_count = 0
    for p in pstrs:
        doc = dict()
        p = p.replace('\n',' ')
        entries = p.split(' ')
        for e in entries:
            key = e.split(':')[0]
            value = e.split(':')[1]
            doc[key] = value
        has_keys = [x for x in doc.keys() if not x == 'cid']
        valid = True
        if set(has_keys) == set(valid_keys):
            byr = int(doc['byr'])
            iyr = int(doc['iyr'])
            eyr = int(doc['eyr'])

            if not (byr >= 1920 and byr <= 2002 and iyr >= 2010 and iyr <= 2020 and
                eyr >= 2020 and eyr <= 2030):
                valid = False

            hgt_units = doc['hgt'][-2:]
            if hgt_units == 'cm':
                hgt = int(doc['hgt'][:-2])
                if not(hgt >= 150 and hgt <= 193):
                    valid = False
            elif hgt_units == 'in':
                hgt = int(doc['hgt'][:-2])
                if not(hgt >= 59 and hgt <= 76):
                    valid = False
            else:
                valid = False

            if doc['hcl'][0] == '#':
                rest = doc['hcl'][1:]
                if len(rest) == 6:
                    try:
                        tst = int(rest,16)
                    except ValueError as e:
                        valid = False
                else:
                    valid = False
            else:
                valid = False

            ecl = doc['ecl']
            eyes = ['amb','blu','brn','gry','grn','hzl','oth']
            if not ecl in eyes:
                valid = False

            pid = doc['pid']
            if not (pid.isdigit() and len(pid) == 9):
                valid = False
        else:
            valid = False

        if valid:
            v_count += 1

    print(v_count)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
