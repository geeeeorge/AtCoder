N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

max_r = 0
max_r_c = 0
one_c = C[0]
flag = True
for i in range(N):
    if C[i] == T:
        if flag:
            flag = False
        max_r = max(max_r, R[i])
    if flag:
        if C[i] == one_c:
            max_r_c = max(max_r_c, R[i])

if max_r != 0:
    print(R.index(max_r) + 1)
else:
    print(R.index(max_r_c) + 1)
