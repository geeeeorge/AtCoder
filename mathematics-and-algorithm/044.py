from collections import deque


def bfs(graph, start):
    """
    幅優先探索
    キューを用いて、グラフを探索する
    各ノードへの最短距離を返す
    """
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


if __name__ == '__main__':
    N, M = map(int, input().split())

    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    ans = bfs(G, 0)
    for i in range(N):
        print(ans[i])
