H, W = map(int, input().split())
S = [input() for _ in range(H)]

# 白いマスの数をカウント
cnt = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            cnt += 1

# 幅優先探索
from collections import deque
q = deque()
q.append((0, 0))
dist = [[-1] * W for _ in range(H)]
dist[0][0] = 1
while q:
    x, y = q.popleft()
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        # ダメな場合
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if S[nx][ny] == '#':
            continue

        if dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
print(cnt - dist[H-1][W-1] if dist[H-1][W-1] != -1 else -1)
