N = int(input())
S = input()

flag = True
now = S[0]
for i in range(1, N):
    if now == S[i]:
        flag = False
        break
    now = S[i]

print('Yes' if flag else 'No')
