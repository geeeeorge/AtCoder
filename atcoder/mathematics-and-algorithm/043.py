def dfs(graph, start):
    visited = set()  # 訪問済みノードを管理するための集合
    stack = [start]  # スタックを初期化して、スタートノードを追加する

    while stack:
        node = stack.pop()  # スタックから次に探索するノードを取り出す
        if node not in visited:  # まだ訪問していない場合は、訪問済みノードに追加する
            visited.add(node)
            for neighbor in graph[node]:  # 隣接するノードをスタックに追加する
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited


if __name__ == '__main__':
    N, M = map(int, input().split())

    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)

    ans = dfs(G, 0)
    if len(ans) == N:
        print('The graph is connected.')
    else:
        print('The graph is not connected.')
