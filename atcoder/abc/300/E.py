N = int(input())

c2, c3, c5 = 0, 0, 0
while N % 2 == 0:
    N //= 2
    c2 += 1
while N % 3 == 0:
    N //= 3
    c3 += 1
while N % 5 == 0:
    N //= 5
    c5 += 1
if N != 1:
    print(0)
    exit()

mod = 998244353
inv5 = pow(5, mod-2, mod)
dp = [[[0] * (c5 + 5) for _ in range(c3 + 5)] for _ in range(c2 + 5)]
dp[0][0][0] = 1
for i in range(c2 + 1):
    for j in range(c3 + 1):
        for k in range(c5 + 1):
            if dp[i][j][k] == 0:
                continue
            dp[i+1][j][k] += dp[i][j][k] * inv5
            dp[i][j+1][k] += dp[i][j][k] * inv5
            dp[i+2][j][k] += dp[i][j][k] * inv5
            dp[i][j][k+1] += dp[i][j][k] * inv5
            dp[i+1][j+1][k] += dp[i][j][k] * inv5
print(dp[c2][c3][c5] % mod)
