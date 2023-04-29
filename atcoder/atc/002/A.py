from collections import deque


# 幅優先探索でも解ける
def bfs(graph, start, goal) -> int:
    dist = [[-1] * W for _ in range(H)]
    dist[start[0]][start[1]] = 0
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for i, j in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:

            # 壁か
            if graph[i][j] == '#':
                continue

            # 既に訪れているか
            if dist[i][j] == -1:
                queue.append((i, j))
                dist[i][j] = dist[x][y] + 1
                if (i, j) == goal:
                    return dist[i][j]


if __name__ == "__main__":
    H, W = map(int, input().split())
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())
    G = [[] for _ in range(H)]
    s = (sx-1, sy-1)
    g = (gx-1, gy-1)
    for i in range(H):
        a = input()
        for j in range(W):
            G[i].append(a[j])

    dst = bfs(G, s, g)
    print(dst)
