N, K = map(int, input().split())
A = list(map(int, input().split()))

# dp[i] := 最後からi番目に勝ち確定なら1、負け確定なら0
dp = [0] * (N + 1)

for i in range(N):
    if dp[i] == 1:
        continue
    for ai in A:
        if i + ai <= N:
            dp[i + ai] = 1

print('First' if dp[-1] else 'Second')
