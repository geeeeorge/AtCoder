def dfs(graph, start):
    """
    深さ優先探索
    スタックを用いて、グラフを探索する
    訪問済みノードの集合を返す
    """
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
