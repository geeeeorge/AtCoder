N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dpで解く
dp = [101] * N
dp[0] = 0
dp[1] = A[0]
for i in range(2, N):
    dp[i] = min(dp[i - 1] + A[i - 1], dp[i - 2] + B[i - 2])
print(dp[-1])
