N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dpで解く
dp = [101] * N
dp[0] = 0
dp[1] = A[0]
for i in range(2, N):
    dp[i] = min(dp[i-1] + A[i-1], dp[i-2] + B[i-2])

# 経路を復元する
ans = [N]
i = N - 1
while i > 0:
    if dp[i] == dp[i-1] + A[i-1]:
        ans.append(i)
        i -= 1
    else:
        ans.append(i-1)
        i -= 2
ans.reverse()
print(len(ans))
print(*ans)
