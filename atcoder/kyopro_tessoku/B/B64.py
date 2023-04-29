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

dst = dijkstra(G, 0)
# 最短経路を逆算する
ans = [N]
v = N - 1
while v != 0:
    for to, cost in G[v]:
        if dst[v] == dst[to] + cost:
            ans.append(to + 1)
            v = to
            break
ans.reverse()
print(*ans)
