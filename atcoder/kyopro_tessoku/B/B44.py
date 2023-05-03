N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # 行交換
        x = query[1] - 1
        y = query[2] - 1
        A[x], A[y] = A[y], A[x]
    elif query[0] == 2:
        # 表示
        x = query[1] - 1
        y = query[2] - 1
        print(A[x][y])
