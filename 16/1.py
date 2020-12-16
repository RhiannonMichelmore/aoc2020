import sys

def check(num,rule_list):
    found = False
    for (l,h) in rule_list:
        if num >= l and num <= h:
            found = True

    return found

def main(in_string):
    sections = in_string.split('\n\n')
    rules = dict()
    for r in sections[0].split('\n'):
        name = r.split(':')[0]
        ranges = r.split(':')[1].strip()
        range1 = ranges.split(' or ')[0]
        range2 = ranges.split(' or ')[1]
        r1_l = int(range1.split('-')[0])
        r1_h = int(range1.split('-')[1])
        r2_l = int(range2.split('-')[0])
        r2_h = int(range2.split('-')[1])
        rules[name] = [(r1_l,r1_h),(r2_l,r2_h)]
    
    total_includes = []
    for k in rules.keys():
        total_includes += rules[k]

    incorrect = []
    for nb in sections[2].split('\n')[1:]:
        numbers = list(map(int,nb.split(',')))
        for n in numbers:
            if not check(n,total_includes):
                incorrect.append(n)

    print(incorrect,sum(incorrect))

    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
