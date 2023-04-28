N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp
dp = [0] * N
for i in range(N-1):
    dp[A[i] - 1] = max(dp[A[i] - 1], dp[i] + 100)
    dp[B[i] - 1] = max(dp[B[i] - 1], dp[i] + 150)
print(dp[-1])
