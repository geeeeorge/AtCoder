n, m = map(int, input().split())
g = [[0] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# bfsで最短経路を求める
from collections import deque


def bfs(s):
    dist = [-1] * (n + 1)
    dist[s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        for nv in g[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    return dist


dists = [0] + [bfs(i) for i in range(1, n + 1)]
ans = [1] * (n + 1)  # 0が白,1が黒
check = []
k = int(input())
for _ in range(k):
    p, d = map(int, input().split())

    # pからの距離がd未満なら白
    for i in range(1, n + 1):
        if dists[p][i] < d:
            ans[i] = 0
    check.append((p, d))

# check
for p, d in check:
    ok = False
    for i in range(1, n + 1):
        if dists[p][i] == d and ans[i] == 1:
            ok = True
            break
    if not ok:
        print('No')
        exit()

print('Yes')
print(*ans[1:], sep='')
