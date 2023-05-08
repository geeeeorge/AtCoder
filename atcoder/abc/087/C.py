N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]

dp = [[0] * N for _ in range(2)]
# 1行目
dp[0][0] = A[0][0]
for i in range(1, N):
    dp[0][i] = dp[0][i - 1] + A[0][i]

# 2行目
dp[1][0] = dp[0][0] + A[1][0]
for i in range(1, N):
    dp[1][i] = max(dp[0][i], dp[1][i - 1]) + A[1][i]
print(dp[1][N - 1])
