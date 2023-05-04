N, M = map(int, input().split())

G = [set() for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)

ans_idx = 0
max_len = 0
for i in range(1, N+1):
    if len(G[i]) > max_len:
        ans_idx = i
        max_len = len(G[i])

print(ans_idx)
