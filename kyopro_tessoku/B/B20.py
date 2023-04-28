S = input()
T = input()

# 編集距離
# dp[i][j] := Sのi文字目までとTのj文字目までの編集距離
dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
# 初期化
for i in range(len(S) + 1):
    dp[i][0] = i
for j in range(len(T) + 1):
    dp[0][j] = j

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i + 1][j + 1] = min(dp[i][j + 1] + 1, dp[i + 1][j] + 1, dp[i][j])
        else:
            dp[i + 1][j + 1] = min(dp[i][j + 1] + 1, dp[i + 1][j] + 1, dp[i][j] + 1)

print(dp[-1][-1])
