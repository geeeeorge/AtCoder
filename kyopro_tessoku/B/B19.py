N, max_W = map(int, input().split())
W = []
V = []
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

# 二次元dp、ナップザック問題
# dp[i][j] = i番目までの品物から価値がjになるように選んだ時の重さの最小値
dp = [[float('inf')] * (sum(V)+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for j in range(sum(V)+1):
        if j >= V[i]:
            dp[i+1][j] = min(dp[i][j], dp[i][j-V[i]] + W[i])
        else:
            dp[i+1][j] = dp[i][j]
print(max([j for j in range(sum(V)+1) if dp[-1][j] <= max_W]))
