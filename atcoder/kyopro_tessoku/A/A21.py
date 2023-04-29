N = int(input())
P = []
A = []
for _ in range(N):
    p, a = map(int, input().split())
    P.append(p)
    A.append(a)

# 区間DP
# dp[l][r] := l番目からr番目までのブロックが残っているときの得点の最大値
dp = [[0] * (N + 1) for _ in range(N + 1)]
for l in range(1, N):
    for r in range(N, l, -1):
        # 左端を取る場合
        s1 = 0
        if l <= P[l - 1] <= r:
            s1 += A[l - 1]
        # 右端を取る場合
        s2 = 0
        if l <= P[r - 1] <= r:
            s2 += A[r - 1]

        dp[l + 1][r] = max(dp[l + 1][r], dp[l][r] + s1)
        dp[l][r - 1] = max(dp[l][r - 1], dp[l][r] + s2)

ans = 0
for i in range(1, N + 1):
    ans = max(dp[i][i], ans)
print(ans)
