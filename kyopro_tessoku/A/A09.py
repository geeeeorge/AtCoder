H, W, N = map(int, input().split())

l = [[0] * (W + 1) for _ in range(H + 1)]

for _ in range(N):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1

    # 二次元いもす法
    l[a][b] += 1
    l[a][d+1] -= 1
    l[c+1][b] -= 1
    l[c+1][d+1] += 1

# 横方向に累積和
for i in range(H):
    for j in range(W):
        l[i][j+1] += l[i][j]

# 縦方向に累積和
for i in range(H):
    for j in range(W):
        l[i+1][j] += l[i][j]

for i in range(H):
    l[i].pop()
    print(*l[i])
