import copy


N = int(input())
A = [list(map(int, list(input().strip()))) for _ in range(N)]

B = copy.deepcopy(A)

B[0][0] = A[1][0]
B[N-1][N-1] = A[N-2][N-1]

for i in range(1, N):
    B[0][i] = A[0][i-1]

for i in range(1, N-1):
    B[i][0] = A[i+1][0]
    B[i][N-1] = A[i-1][N-1]

for i in range(0, N-1):
    B[N-1][i] = A[N-1][i+1]

for b in B:
    print(''.join(map(str, b)))
