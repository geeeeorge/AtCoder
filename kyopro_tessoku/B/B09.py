N = int(input())

A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
W = max(C)
H = max(D)
l = [[0] * (W+1) for _ in range(H+1)]

# 二次元いもす法
for i in range(N):
    l[B[i]][A[i]] += 1
    l[D[i]][A[i]] -= 1
    l[B[i]][C[i]] -= 1
    l[D[i]][C[i]] += 1

# 横方向に累積和
for i in range(H):
    for j in range(W):
        l[i][j+1] += l[i][j]

# 縦方向に累積和
for i in range(H):
    for j in range(W):
        l[i+1][j] += l[i][j]

# 重なっている部分の数を数える
ans = 0
for i in range(H):
    for j in range(W):
        if l[i][j] > 0:
            ans += 1
print(ans)
