S = input()
T = input()

l = [i for i in 'atcoder']

for i in range(len(S)):
    if S[i] == T[i]:
        continue
    elif S[i] == '@' and T[i] in l:
        continue
    elif T[i] == '@' and S[i] in l:
        continue
    else:
        print('You will lose')
        break
else:
    print('You can win')
