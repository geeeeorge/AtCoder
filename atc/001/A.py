def dfs(graph, start, goal) -> bool:
    stack = [start]
    visited = set()
    while stack:
        x, y = stack.pop()
        for i, j in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            # グラフからはみ出してないか
            if not(0 <= i < H and 0 <= j < W):
                continue

            # 壁か
            if graph[i][j] == '#':
                continue

            # 既に訪れているか
            if (i, j) not in visited:
                if (i, j) == goal:
                    return True
                stack.append((i, j))
                visited.add((i, j))
    return False


if __name__ == "__main__":
    H, W = map(int, input().split())
    G = [[] for _ in range(H)]
    s = ()
    g = ()
    for i in range(H):
        a = input()
        for j in range(W):
            if a[j] == 's':
                s = (i, j)
            if a[j] == 'g':
                g = (i, j)
            G[i].append(a[j])

    b = dfs(G, s, g)
    print('Yes' if b else 'No')
