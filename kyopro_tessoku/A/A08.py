H, W = map(int, input().split())
X = [[] for _ in range(H)]

for i in range(H):
    X[i] = list(map(int, input().split()))

# 2次元累積和
S = [[0] * (W + 1) for _ in range(H + 1)]
# 横方向に累積和
for i in range(H):
    for j in range(W):
        S[i + 1][j + 1] = S[i + 1][j] + X[i][j]
# 縦方向に累積和
for i in range(H):
    for j in range(W):
        S[i + 1][j + 1] += S[i][j + 1]

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(S[c][d] - S[a - 1][d] - S[c][b - 1] + S[a - 1][b - 1])
