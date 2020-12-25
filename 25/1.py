import sys

def main(in_string):
    card_pub = int(in_string.split('\n')[0])
    door_pub = int(in_string.split('\n')[1])

    sub_num = 7
    val = 1
    c = 0
    while True:
        val = val*sub_num
        val = val % 20201227
        if val == card_pub or val == door_pub:
            print('loop:',c+1)
            break
        c += 1

    if val == card_pub:
        sub_num = door_pub
    else:
        sub_num = card_pub

    val = 1
    for i in range(c+1):
        val = val*sub_num
        val = val % 20201227

    print(val)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
