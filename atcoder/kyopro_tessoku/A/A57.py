N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))

# dp[i][j]: 最初iの穴からj日目の穴の場所
dp = [[0] * (N + 1) for _ in range(32)]
for i in range(1, N + 1):
    dp[0][i] = A[i]
for i in range(1, 32):
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]
for _ in range(Q):
    x, y = map(int, input().split())
    for i in range(31, -1, -1):
        if y & (1 << i):
            x = dp[i][x]
    print(x)
