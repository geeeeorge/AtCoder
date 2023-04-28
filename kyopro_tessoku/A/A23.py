N, M = map(int, input().split())
A = []
for i in range(M):
    a = list(map(int, input().split()))
    A.append(a)

# bitDP
dp = [[1009] * (1 << N) for _ in range(M+1)]
dp[0][0] = 0

for i in range(M):
    for j in range(1 << N):
        # jからどこが無料なのかを調べる
        already = [0] * N
        j_b = bin(j)[2:]
        for k in range(len(j_b)):
            if j_b[k] == "1":
                already[len(j_b) - 1 - k] = 1

        # クーポンを使った際のj(v)を計算
        v = 0
        for k in range(N):
            if already[k] == 1 or A[i][k] == 1:
                v += 1 << k

        # クーポンを使わない時
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        # クーポンを使う時
        dp[i+1][v] = min(dp[i+1][v], dp[i][j] + 1)

if dp[-1][-1] == 1009:
    print(-1)
else:
    print(dp[-1][-1])

