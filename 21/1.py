import sys
import itertools
import copy

def main(in_string):
    possibilities = dict()
    pairs = []
    ings = []
    alls = []
    for line in in_string.split('\n'):
        ingridients = line.split('(')[0].strip().split(' ')
        allergens = [x.strip() for x in line.split('(')[1][9:-1].split(',')]
        for allergen in allergens:
            alls.append(allergen)
            if not allergen in possibilities:
                possibilities[allergen] = set()
        for ingridient in ingridients:
            ings.append(ingridient)
        pairs.append((allergens,ingridients))

    alls = list(set(alls))
    ings = list(set(ings))

    possible = []
    for allergen in alls:
        ig_lists = []
        for (als,igs) in pairs:
            if allergen in als:
                ig_lists.append(set(igs))
        common = set.intersection(*ig_lists)
        possibilities[allergen] = common
        possible += list(common)

    possible = list(set(possible))
    not_possible = [i for i in ings if i not in possible]

    count = 0
    for (als,igs) in pairs:
        for np in not_possible:
            if np in igs:
                count += 1

    print(count)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
