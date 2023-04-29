N = int(input())

mod = 10 ** 9 + 7

# フィボナッチ数列
# dp[i] = i番目のフィボナッチ数
dp = [0] * N
dp[0] = 1
dp[1] = 1
for i in range(2, N):
    dp[i] = (dp[i - 1] + dp[i - 2]) % mod
print(dp[-1])
