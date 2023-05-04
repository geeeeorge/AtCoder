N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

# stackでdfsし，経路復元
# 1からNにたどり着けば良い
stack = [0]
visited = [False] * N
visited[0] = True
prev = [-1] * N
while stack:
    v = stack.pop()
    for to in G[v]:
        if not visited[to]:
            visited[to] = True
            prev[to] = v
            stack.append(to)

if prev[N-1] == -1:
    print('No')
else:
    ans = []
    v = N-1
    while v != -1:
        ans.append(v+1)
        v = prev[v]
    print(*ans[::-1])
