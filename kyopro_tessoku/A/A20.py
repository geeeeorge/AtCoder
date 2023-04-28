S = input()
T = input()

# LCS
# 最長共通部分列問題
# dp[i][j] := Sのi文字目までとTのj文字目までのLCSの長さ
dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[-1][-1])
