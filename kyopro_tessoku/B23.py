N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


def dist(a, b):
    return ((X[a] - X[b]) ** 2 + (Y[a] - Y[b]) ** 2) ** 0.5


# bitDP
# 巡回セールスマン問題
# dp[i][j]: i番目の都市にいて、jの都市を訪れた時の最小コスト
dp = [[float("inf")] * N for _ in range(1 << N)]
dp[0][0] = 0

for i in range(1 << N):
    for j in range(N):
        if dp[i][j] == float("inf"):
            continue

        for k in range(N):
            # すでに訪れている都市はスキップ
            if i & 1 << k:
                continue
            # 訪れていない都市を訪れる
            dp[i | 1 << k][k] = min(dp[i | 1 << k][k], dp[i][j] + dist(j, k))

print(dp[-1][0])
