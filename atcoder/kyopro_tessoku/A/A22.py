N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp
# dpの初期化の際に0で初期化していたが、これだとdp[i]が更新されない場合に0になってしまうので、
# dp[i]が更新されない場合にはdp[i]の値をそのままにしておく必要がある。
dp = [-10**8] * N
dp[0] = 0
for i in range(N-1):
    dp[A[i] - 1] = max(dp[A[i] - 1], dp[i] + 100)
    dp[B[i] - 1] = max(dp[B[i] - 1], dp[i] + 150)
print(dp[-1])
