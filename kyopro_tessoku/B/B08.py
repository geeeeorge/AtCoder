N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
max_x = max(X)
max_y = max(Y)
H, W = max_x, max_y

# 二次元累積和
K = [[0] * W for _ in range(H)]
S = [[0] * (W + 1) for _ in range(H + 1)]

# K作成
for i in range(N):
    K[X[i] - 1][Y[i] - 1] += 1

# 横方向に累積和
for i in range(H):
    for j in range(W):
        S[i + 1][j + 1] = S[i + 1][j] + K[i][j]

# 縦方向に累積和
for i in range(H):
    for j in range(W):
        S[i + 1][j + 1] += S[i][j + 1]

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    # max, minでパース
    c = min(c, max_x)
    d = min(d, max_y)
    print(S[c][d] - S[a - 1][d] - S[c][b - 1] + S[a - 1][b - 1])
