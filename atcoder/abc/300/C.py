H, W = map(int, input().split())
C = [input() for _ in range(H)]

# coreを探して、右上にいくつあるか数える
cores = []

for i in range(1, H-1):
    for j in range(1, W-1):
        if C[i][j] != '#':
            continue
        if C[i-1][j-1] == '#' and C[i+1][j-1] == '#' and C[i-1][j+1] == '#' and C[i+1][j+1] == '#':
            cores.append((i, j))

ans = [0] * min(H, W)
for i, j in cores:
    cnt = 0
    while True:
        if 0 <= i-1 and j+1 < W and C[i-1][j+1] == '#':
            cnt += 1
            i -= 1
            j += 1
        else:
            break
    ans[cnt-1] += 1

print(*ans)
