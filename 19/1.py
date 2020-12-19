import sys
import itertools

def main(in_string):
    str_rules = in_string.split('\n\n')[0].split('\n')
    strings = in_string.split('\n\n')[1].split('\n')
    str_rules = sorted(str_rules,key = lambda x: int(x.split(':')[0]))
    rules = []
    for r_str in str_rules:
        r = r_str.split(':')[1].strip()
        r1_str = r.split(' | ')[0]
        if r1_str == '"a"' or r1_str == '"b"':
            to_append = 'a' if r1_str == '"a"' else 'b'
            rules.append([to_append])
        else:
            split = r1_str.split(' ')
            r1 = list(map(int,split))
            to_append = [r1]

            if len(r.split(' | ')) > 1:
                r2_str = r.split(' | ')[1]
                split = r2_str.split(' ')
                r2 = list(map(int,split))
                to_append.append(r2)
            rules.append(to_append)

    rule = 0
    all_strings = gen_all_strings(rule,rules)
    count = 0
    for s in strings:
        if s in all_strings:
            count += 1

    print('Correct:',count)


def gen_all_strings(rule,rules):
    if len(rules[rule]) == 1 and (rules[rule][0] == 'a' or rules[rule][0]=='b'):
        return rules[rule]
    else:
        strings = []
        for or_seq in rules[rule]:
            tmp_strs = []
            for rule_num in or_seq:
                tmp_strs.append(gen_all_strings(rule_num,rules))
            strs = list(itertools.product(*tmp_strs))
            strs = [''.join(s) for s in strs]
            strings += strs
        return strings

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
