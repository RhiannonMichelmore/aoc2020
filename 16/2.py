import sys
import numpy as np
import copy

def check(num,rule_list):
    found = False
    for (l,h) in rule_list:
        if num >= l and num <= h:
            found = True

    return found

def check_list(nums,rule_list):
    valid = True
    for n in nums:
        found = False
        for (l,h) in rule_list:
            if n >= l and n <= h:
                found = True
        if not found:
            valid = False
            break
    return valid

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

    correct = []
    for nb in sections[2].split('\n')[1:]:
        numbers = list(map(int,nb.split(',')))
        if all([check(n,total_includes) for n in numbers]):
            correct.append(numbers)

    # add our ticket
    our_ticket = list(map(int,sections[1].split('\n')[1].split(',')))
    correct.append(our_ticket)
    correct = np.array(correct)

    valid_per_idx = []
    for idx,nums in enumerate(correct.T):
        current_valid_rules = []
        for rule in rules.keys():
            if check_list(nums,rules[rule]):
                current_valid_rules.append(rule)
        valid_per_idx.append((idx,current_valid_rules))

    assignment = []
    alone_rules = []

    while len(alone_rules) < len(rules.keys()):
        changed = False
        new_valid = []
        for (idx,v_rules) in valid_per_idx:
            if len(v_rules) == 1:
                assignment.append((idx,v_rules[0]))
                alone_rules.append(v_rules[0])
            else:
                new_valid.append((idx,v_rules))

        for i,(idx,v_rules) in enumerate(new_valid):
            new_v_rules = []
            for vr in v_rules:
                if not vr in alone_rules:
                    new_v_rules.append(vr)

            new_valid[i] = (idx,new_v_rules)
        valid_per_idx = new_valid

    result = []
    for (idx,rule) in assignment:
        if rule.startswith('departure'):
            result.append(our_ticket[idx])

    print(np.product(result))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
