import sys
import re

def main(in_string):
    exprs = in_string.split('\n')
    total = 0
    for expr in exprs:
        expr = expr.replace(')',' )')
        expr = expr.replace('(','( ')
        tokens = expr.split(' ')
        tokens = [int(x) if x.isnumeric() else x for x in tokens]
        total += calculate(tokens)
    print(total)

def calculate(tokens):
    total = None
    # parse into subexprs
    sub_expr = []
    expr = []
    stack = []
    op = None
    recording_sub = False
    for t in tokens:
        if t == '(':
            stack.append('(')
            recording_sub = True
            if len(stack) > 1:
                sub_expr.append('(')
        elif t == ')':
            stack.pop()
            if len(stack) == 0:
                recording_sub = False
                number = calculate(sub_expr)
                expr.append(number)
                sub_expr = []
            else:
                sub_expr.append(')')
        elif t == '*' or t=='+':
            if recording_sub:
                sub_expr.append(t)
            else:
                expr.append(t)
        else:
            if recording_sub:
                sub_expr.append(t)
            else:
                expr.append(t)

    expr_str = ''.join(list(map(str,expr)))
    expr_str = re.sub(r'^(\d+\+)',r'(\1',expr_str)
    expr_str = re.sub(r'\*(\d+\+)',r'*(\1',expr_str)

    expr_str = re.sub(r'\+(\d+)$',r'+\1)',expr_str)
    expr_str = re.sub(r'\+(\d+)\*',r'+\1)*',expr_str)

    total = eval(expr_str)

    return total
                

        

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No input found.')
    else:
        with open(sys.argv[1],'r') as f:
            in_string = f.read().strip()
            main(in_string)
