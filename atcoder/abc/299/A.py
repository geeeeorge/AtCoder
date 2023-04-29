N = int(input())
S = input()

is_in = False

for s in S:
    if s == '|':
        # is_inを反転
        is_in = not is_in
    if s == '*':
        if is_in:
            print('in')
            break
        else:
            print('out')