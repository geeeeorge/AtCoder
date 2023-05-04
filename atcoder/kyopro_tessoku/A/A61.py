N, M = map(int, input().split())

G = [set() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)

for i in range(1, N+1):
    if len(G[i]):
        print(f'{i}: {G[i]}')
    else:
        print(f'{i}:' + '{}')
