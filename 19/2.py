import sys
import itertools

def main(in_string):
    str_rules = in_string.split('\n\n')[0].split('\n')
    strings = in_string.split('\n\n')[1].split('\n')
    str_rules = sorted(str_rules,key = lambda x: int(x.split(':')[0]))
    rules = dict()
    for r_str in str_rules:
        key = int(r_str.split(':')[0])
        r = r_str.split(':')[1].strip()
        r1_str = r.split(' | ')[0]
        if r1_str == '"a"' or r1_str == '"b"':
            to_append = 'a' if r1_str == '"a"' else 'b'
            rules[key] = [to_append]
        else:
            split = r1_str.split(' ')
            r1 = list(map(int,split))
            to_append = [r1]

            if len(r.split(' | ')) > 1:
                r2_str = r.split(' | ')[1]
                split = r2_str.split(' ')
                r2 = list(map(int,split))
                to_append.append(r2)
            rules[key] = to_append

    rules[8] = [[42],[42,8]]
    rules[11] = [[42,31],[42,11,31]]

    rule42 = gen_all_strings(42,rules)
    rule31 = gen_all_strings(31,rules)

    sec_len = len(rule42[0])

    # 8 11
    count = 0
    for s in strings:
        correct = True
        switched = False
        c42 = 0
        c31 = 0
        for i in range(int(len(s)/sec_len)):
            sector = s[i*sec_len:i*sec_len+sec_len]
            if i == 0:
                if not sector in rule42:
                    correct = False
                    break
                else:
                    c42 += 1
            else:
                if switched == False:
                    if sector in rule42:
                        c42 += 1
                    elif sector in rule31:
                        if i == 1:
                            correct = False
                            break
                        else:
                            c31 += 1
                            switched = True
                    else:
                        correct = False
                        break
                else:
                    if sector in rule31:
                        c31 += 1
                    else:
                        correct = False
                        break
        
        if correct and switched and c42 > c31:
            count += 1

    print(count)

def gen_all_strings(rule,rules):
    if len(rules[rule]) == 1 and (rules[rule][0] == 'a' or rules[rule][0]=='b'):
        return rules[rule]
    else:
        strings = []
        for or_seq in rules[rule]:
            tmp_strs = []
            for rule_num in or_seq:
                if rule_num == 8:
                    tmp_strs.append([str(8)])
                elif rule_num == 11:
                    tmp_strs.append([str(1)])
                else:
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
