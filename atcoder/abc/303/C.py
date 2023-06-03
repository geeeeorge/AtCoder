N, M, H, K = map(int, input().split())
S = input()
x_i = []
y_i = []
for i in range(M):
    x, y = map(int, input().split())
    x_i.append(x)
    y_i.append(y)

d = {}
for i in range(M):
    if not d.get(x_i[i]):
        d[x_i[i]] = set()
    d[x_i[i]].add(y_i[i])


ans = True
x = 0
y = 0

for i in range(N):
    H -= 1
    cmd = S[i]
    if cmd == 'R':
        x += 1
    if cmd == 'L':
        x -= 1
    if cmd == 'U':
        y += 1
    if cmd == 'D':
        y -= 1

    if H < 0:
        ans = False
        break
    elif 0 <= H < K:
        if d.get(x) and y in d[x]:
            H = K
            d[x].remove(y)

print('Yes' if ans else 'No')
