N1, N2, M = map(int, input().split())
G1 = [[] for _ in range(N1)]
G2 = [[] for _ in range(N2)]
for i in range(M):
    a, b = map(int, input().split())
    if a <= N1:
        G1[a - 1].append(b - 1)
        G1[b - 1].append(a - 1)
    else:
        G2[a - N1 - 1].append(b - N1 - 1)
        G2[b - N1 - 1].append(a - N1 - 1)

def bfs(graph, start):
    from collections import deque

    dist = [-1] * len(graph)  # 各ノードへの最短距離を格納するリスト
    dist[start] = 0  # スタートノードの距離は0とする
    queue = deque([start])  # キューを初期化して、スタートノードを追加する

    while queue:
        node = queue.popleft()  # キューから次に探索するノードを取り出す
        for neighbor in graph[node]:  # 隣接するノードをキューに追加する
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return dist


dist1 = bfs(G1, 0)
dist2 = bfs(G2, N2-1)
print(max(dist1) + max(dist2) + 1)
