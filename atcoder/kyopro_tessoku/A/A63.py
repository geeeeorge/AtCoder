N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

# bfsで，頂点0からの距離を求める
from collections import deque
dist = [-1] * N
dist[0] = 0
q = deque([0])
while q:
    v = q.popleft()
    for to in G[v]:
        if dist[to] != -1:
            continue
        dist[to] = dist[v] + 1
        q.append(to)
for i in range(N):
    print(dist[i])
