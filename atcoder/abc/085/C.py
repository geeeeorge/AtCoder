N, Y = map(int, input().split())
A = Y / 1000

for x in range(N + 1):
    for y in range(N - x + 1):
        if 9 * x + 4 * y == A - N:
            print(x, y, N-x-y)
            exit()
print(-1, -1, -1)
