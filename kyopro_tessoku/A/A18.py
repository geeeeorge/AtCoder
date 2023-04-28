N, S = map(int, input().split())
A = list(map(int, input().split()))

# 二次元dp、部分和問題
# dp[i][j] := i番目までの整数の中からいくつか選んで総和をjにできるか
dp = [[False] * (S+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    for j in range(S+1):
        if dp[i][j]:
            dp[i+1][j] = True
        if j >= A[i] and dp[i][j-A[i]]:
            dp[i+1][j] = True

print('Yes' if dp[-1][-1] else 'No')
