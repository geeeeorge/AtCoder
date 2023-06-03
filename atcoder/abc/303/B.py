N, M = map(int, input().split())
A = []
for i in range(M):
    A.append(list(map(int, input().split())))

d = {}
for i in range(N):
    d[i+1] = set()

for i in range(M):
    for j in range(N-1):
        d[A[i][j]].add(A[i][j+1])
        d[A[i][j+1]].add(A[i][j])

cnt = 0
for i in range(N):
    cnt += N - 1 - len(d[i+1])

print(cnt // 2)
