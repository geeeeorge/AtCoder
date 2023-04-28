N, S = map(int, input().split())
A = list(map(int, input().split()))

# 二次元dp、部分和問題
# dp[i][j] := i番目までの要素でjを作ることができるか
dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True
for i in range(N):
    for j in range(S + 1):
        if dp[i][j]:
            dp[i + 1][j] = True
        elif j >= A[i] and dp[i][j - A[i]]:
            dp[i + 1][j] = True

# 経路復元
if not dp[-1][-1]:
    print(-1)
    exit()
ans = []
i = N
j = S
while i > 0:
    if dp[i - 1][j]:
        i -= 1
    else:
        ans.append(i)
        j -= A[i - 1]
        i -= 1
ans.reverse()
print(len(ans))
print(*ans)
