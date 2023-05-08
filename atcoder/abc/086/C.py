N = int(input())

time = 0
x, y = 0, 0

ans = True
for i in range(N):
    t, nx, ny = map(int, input().split())
    dt = t - time
    dist = abs(nx - x) + abs(ny - y)
    if dt < dist or (dt - dist) % 2 == 1:
        ans = False
    time = t
    x, y = nx, ny
print('Yes' if ans else 'No')
