N = int(input())
A, B = [], []
for i in range(N):
    A.append(list(map(int, input().split())))
for i in range(N):
    B.append(list(map(int, input().split())))

ans = False
# 4回転まで
for _ in range(4):
    rotA = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                rotA[N-1-j][i] = 1
    flag = False
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and B[i][j] != 1:
                flag = True
                break
        if flag:
            break
    if not flag:
        ans = True
        break
    A = rotA
print('Yes' if ans else 'No')
