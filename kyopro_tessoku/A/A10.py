N = int(input())
A = list(map(int, input().split()))

D = int(input())

l_A_max = [0] * N
r_A_max = [0] * N
# 左から累積max
for i in range(N-1):
    l_A_max[i+1] = max(l_A_max[i], A[i])
# 右から累積max
for i in range(N-1, 0, -1):
    r_A_max[i-1] = max(r_A_max[i], A[i])

for _ in range(D):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    if l == 0:
        print(r_A_max[r])
    elif r == N-1:
        print(l_A_max[l])
    else:
        print(max(l_A_max[l], r_A_max[r]))
