H, W = map(int, input().split())
C = [[] for _ in range(H)]
for i in range(H):
    c = input()
    for j in range(W):
        C[i].append(c[j])

# dp[i][j] = (i, j)に到達するための方法の数
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if i + 1 < H and C[i + 1][j] == '.':
            dp[i + 1][j] += dp[i][j]
        if j + 1 < W and C[i][j + 1] == '.':
            dp[i][j + 1] += dp[i][j]

print(dp[-1][-1])
