def dijkstra(graph, start):
    import heapq

    n = len(graph)
    visited = [False] * n
    dist = [float('inf')] * n
    dist[start] = 0
    # (距離, 頂点)の順で格納
    hq = [(0, start)]
    heapq.heapify(hq)

    while hq:
        d, v = heapq.heappop(hq)
        if visited[v]:
            continue

        # vを確定
        visited[v] = True

        for to, cost in graph[v]:
            if not visited[to] and dist[v] + cost < dist[to]:
                # dist更新
                dist[to] = dist[v] + cost
                # ヒープに追加
                heapq.heappush(hq, (dist[to], to))
    return dist


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, c))
    G[b].append((a, c))

ans = dijkstra(G, 0)
for i in range(N):
    if ans[i] == float('inf'):
        print(-1)
    else:
        print(ans[i])
