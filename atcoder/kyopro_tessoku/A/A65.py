N = int(input())
A = list(map(int, input().split()))

G = [list() for _ in range(N+1)]
for i, a in enumerate(A):
    G[a].append(i+2)

dp = [0] * (N+1)
for i in range(N, 0, -1):
    if len(G[i]) == 0:
        dp[i] = 0
    else:
        for j in G[i]:
            dp[i] += dp[j] + 1
for i in range(1, N+1):
    print(dp[i], end=" ")
print()
