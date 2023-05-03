N, C = map(str, input().split())
N = int(N)
tmp = input()
A = []
for i in range(N):
    A.append(tmp[i])

d= {'W': 0, 'B': 1, 'R': 2}

score = 0
for a in A:
    if a == 'W':
        continue
    elif a == 'B':
        score += d['B']
    else:
        score += d['R']

ans = [k for k, v in d.items() if v == score % 3]

if ans[0] == C:
    print('Yes')
else:
    print('No')

