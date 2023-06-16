H, W = map(int, input().split())
s = [input() for _ in range(H)]

u = H - 1
d = 0
l = W - 1
r = 0

for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            u = min(u, i)
            d = max(d, i)
            l = min(l, j)
            r = max(r, j)

for i in range(u, d + 1):
    for j in range(l, r + 1):
        if s[i][j] != '#':
            print(i+1, j+1)
            exit()
