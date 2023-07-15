R, C = map(int, input().split())
B = [list(input()) for i in range(R)]

num = [str(i) for i in range(1, 10)]

bombs = []
for i in range(R):
    for j in range(C):
        if B[i][j] in num:
            bombs.append((int(B[i][j]), i, j))

for b, i, j in bombs:
    for k in range(R):
        for l in range(C):
            dis = abs(i-k) + abs(j-l)
            if dis <= b:
                B[k][l] = '.'
for row in B:
    print(''.join(row))
