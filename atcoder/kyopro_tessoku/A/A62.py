N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

# stackでdfs
stack = [0]
visited = [False] * N
visited[0] = True
while stack:
    v = stack.pop()
    for to in G[v]:
        if visited[to]:
            continue
        visited[to] = True
        stack.append(to)
if all(visited):
    print("The graph is connected.")
else:
    print("The graph is not connected.")
