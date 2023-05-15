N = int(input())
S = input()

flag1 = False
flag2 = False
for i in range(N):
    if S[i] == 'o':
        flag1 = True
    if S[i] == 'x':
        flag2 = True
print('Yes' if flag1 and not flag2 else 'No')
