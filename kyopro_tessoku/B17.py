N = int(input())
H = list(map(int, input().split()))

# dp
dp = [0] * N
dp[1] = abs(H[1] - H[0])
for i in range(2, N):
    dp[i] = min(dp[i-1] + abs(H[i] - H[i-1]), dp[i-2] + abs(H[i] - H[i-2]))

# 経路復元
ans = [N]
i = N - 1
while i > 0:
    if dp[i] == dp[i-1] + abs(H[i] - H[i-1]):
        ans.append(i)
        i -= 1
    else:
        ans.append(i-1)
        i -= 2
ans.reverse()
print(len(ans))
print(*ans)
