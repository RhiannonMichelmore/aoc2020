import sys

def main(in_string):
    players = in_string.split('\n\n')
    player_1 = list(map(int,players[0].split('\n')[1:]))
    player_2 = list(map(int,players[1].split('\n')[1:]))

    _, winner = play_game(player_1,player_2)

    score = 0
    for index,card in enumerate(winner):
        multiplier = len(winner)-index
        score += multiplier * card

    print('Score:',score)

# returns the winner and winners deck
def play_game(p1_deck,p2_deck):
    states = dict()
    p1d = p1_deck.copy()
    p2d = p2_deck.copy()

    states[str((p1d,p2d))] = 1

    while len(p1d) > 0 and len(p2d) > 0:
        if str((p1d,p2d)) in states.keys():
            if states[str((p1d,p2d))] > 1:
                return 1, p1d
        p1 = p1d.pop(0)
        p2 = p2d.pop(0)
        if len(p1d) >= p1 and len(p2d) >= p2:
            # recurse
            winner, winner_deck = play_game(p1d[:p1],p2d[:p2])
        else:
            if p1 > p2:
                winner = 1
            else:
                winner = 2

        if winner == 1:
            p1d.append(p1)
            p1d.append(p2)
        else:
            p2d.append(p2)
            p2d.append(p1)

        if not str((p1d,p2d)) in states.keys():
            states[str((p1d,p2d))] = 1
        else:
            states[str((p1d,p2d))] += 1

    if len(p1d) > 0:
        return 1, p1d
    else:
        return 2, p2d

    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
