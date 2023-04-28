N, max_W = map(int, input().split())
W = []
V = []
for i in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

# 二次元dp、ナップザック問題
# dp[i][j] = i番目までの品物から重さがjになるように選んだ時の価値の最大値
dp = [[0] * (max_W+1) for _ in range(N+1)]
for i in range(N):
    for j in range(max_W+1):
        if j >= W[i]:
            dp[i+1][j] = max(dp[i][j], dp[i][j-W[i]] + V[i])
        else:
            dp[i+1][j] = dp[i][j]
print(max(dp[-1]))
