def dijkstra(graph, start):
    """
    ダイクストラ法
    """
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
