N, K = map(int, input().split())

# dp[i][j]: 最初iの数からj回操作したときの数
# 操作は数iの各桁の数の和をiから引く
dp = [[0] * 32 for _ in range(N + 1)]
for i in range(1, N + 1):
    dp[i][0] = i - sum(map(int, str(i)))

for j in range(1, 32):
    for i in range(1, N + 1):
        dp[i][j] = dp[dp[i][j - 1]][j - 1]

for i in range(1, N + 1):
    x = i
    for j in range(31, -1, -1):
        if K & (1 << j):
            x = dp[x][j]
    print(x)
