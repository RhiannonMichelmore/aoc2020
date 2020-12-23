import sys

def main(in_string):
    players = in_string.split('\n\n')
    player_1 = list(map(int,players[0].split('\n')[1:]))
    player_2 = list(map(int,players[1].split('\n')[1:]))

    r = 0

    while len(player_1) > 0 and len(player_2) > 0:
        p1 = player_1.pop(0)
        p2 = player_2.pop(0)
        if p1 > p2:
            player_1.append(p1)
            player_1.append(p2)
        else:
            player_2.append(p2)
            player_2.append(p1)
        r += 1

    print('Rounds:',r)
    winner = None
    if len(player_1) > 0:
        winner = player_1
    else:
        winner = player_2

    score = 0
    for index,card in enumerate(winner):
        multiplier = len(winner)-index
        score += multiplier * card

    print('Score:',score)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
