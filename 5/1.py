
import sys

def main(in_string):
    boards = in_string.split('\n')
    max_id = -1
    for bp in boards:
        upper_row = 127
        lower_row = 0
        diff_row = 128

        upper_col = 7
        lower_col = 0
        diff_col = 8

        row_no = -1
        col_no = -1
        seat_id = -1
        for letter in bp:
            if letter == 'F':
                diff_row = int(diff_row/2)
                if diff_row == 1:
                    row_no = lower_row
                else:
                    upper_row = upper_row - diff_row
            elif letter == 'B':
                diff_row = int(diff_row/2)
                if diff_row == 1:
                    row_no = upper_row
                else:
                    lower_row = lower_row + diff_row
            elif letter == 'R':
                diff_col = int(diff_col/2)
                if diff_col == 1:
                    col_no = upper_col
                else:
                    lower_col = lower_col + diff_col
            elif letter == 'L':
                diff_col = int(diff_col/2)
                if diff_col == 1:
                    col_no = lower_col
                else:
                    upper_col = upper_col - diff_col

        seat_id = (row_no*8)+col_no
        if seat_id > max_id:
            max_id = seat_id

    print(max_id)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
