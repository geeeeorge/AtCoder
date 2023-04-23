from collections import deque


# 幅優先探索でも解ける
def bfs(graph, start, goal) -> bool:
    dist = [[-1] * W for _ in range(H)]
    dist[start[0]][start[1]] = 0
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for i, j in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
            # グラフからはみ出してないか
            if not(0 <= i < H and 0 <= j < W):
                continue

            # 壁か
            if graph[i][j] == '#':
                continue

            # 既に訪れているか
            if dist[i][j] == -1:
                if (i, j) == goal:
                    return True
                queue.append((i, j))
                dist[i][j] = dist[x][y] + 1
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

    b = bfs(G, s, g)
    print('Yes' if b else 'No')
