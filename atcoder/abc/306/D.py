N = int(input())
X, Y = [], []
inf = 10 ** 9 + 7
dp = [[-inf] * 2 for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
for i in range(N):
    if X[i] == 0:
        dp[i + 1][0] = max(dp[i][0], dp[i][0] + Y[i], dp[i][1] + Y[i])
        dp[i + 1][1] = dp[i][1]
    else:
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = max(dp[i][0] + Y[i], dp[i][1])
print(max(dp[N][0], dp[N][1]))
