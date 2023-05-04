R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy, sx, gy, gx = sy-1, sx-1, gy-1, gx-1
maze = [input() for _ in range(R)]

from collections import deque
q = deque([(sy, sx)])
dist = [[-1]*C for _ in range(R)]
dist[sy][sx] = 0
while q:
    y, x = q.popleft()
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny, nx = y+dy, x+dx
        if not (0 <= ny < R and 0 <= nx < C):
            continue
        if maze[ny][nx] == '#':
            continue
        if dist[ny][nx] != -1:
            continue
        dist[ny][nx] = dist[y][x] + 1
        q.append((ny, nx))
print(dist[gy][gx])
