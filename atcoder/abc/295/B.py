R, C = map(int, input().split())
B = [list(input()) for i in range(R)]

num = [str(i) for i in range(1, 10)]

bombs = []
for i in range(R):
    for j in range(C):
        if B[i][j] in num:
            bombs.append((int(B[i][j]), i, j))

for b, i, j in bombs:
    for k in range(b + 1):
        for l in range(b + 1 - k):
            if i - k >= 0 and j + l < C:
                B[i - k][j + l] = '.'
            if i + k < R and j + l < C:
                B[i + k][j + l] = '.'
            if i - k >= 0 and j - l >= 0:
                B[i - k][j - l] = '.'
            if i + k < R and j - l >= 0:
                B[i + k][j - l] = '.'
for row in B:
    print(''.join(row))
