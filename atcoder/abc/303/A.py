N = int(input())
S = input()
T = input()

ans = True
for i in range(N):
    if S[i] == '1' or S[i] == 'l':
        if T[i] != '1' and T[i] != 'l':
            ans = False
    elif S[i] == '0' or S[i] == 'o':
        if T[i] != '0' and T[i] != 'o':
            ans = False
    elif S[i] != T[i]:
        ans = False

print('Yes' if ans else 'No')
