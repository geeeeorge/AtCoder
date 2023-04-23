N = 4
C = []
for i in range(N):
    C.append(list(input().split()))

for i in range(2):
    for j in range(4):
        C[i][j], C[3-i][3-j] = C[3-i][3-j], C[i][j]

for i in range(4):
    print(' '.join(C[i]))
