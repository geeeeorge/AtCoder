N, A, B = map(int, input().split())

# dp
# dp[i] := 最後からi番目が勝ち確定なら1、負け確定なら0
dp = [0] * (N + 1)

for i in range(N):
    if dp[i] == 1:
        continue
    if i + A <= N:
        dp[i + A] = 1
    if i + B <= N:
        dp[i + B] = 1

print('First' if dp[-1] else 'Second')
