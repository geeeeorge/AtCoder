S = input()
gx, gy = map(int, input().split())

# X, Yは独立して考えられる
# dpx[i][x] := x用のi番目のF部分列でxがいけるかどうか
# dpy[i][y] := y用のi番目のF部分列でyがいけるかどうか
# メモリが足りないので、setでやる

A = S.split('T')
X = []
Y = []
for i in range(len(A)):
    if i % 2 == 0:
        X.append(len(A[i]))
    else:
        Y.append(len(A[i]))

dpx = set()
dpx.add(X[0])

for i in range(1, len(X)):
    ndpx = set()
    for x in dpx:
        ndpx.add(x + X[i])
        ndpx.add(x - X[i])
    dpx = ndpx

if gx not in dpx:
    print('No')
    exit()


dpy = set()
dpy.add(0)
for i in range(len(Y)):
    ndpy = set()
    for y in dpy:
        ndpy.add(y + Y[i])
        ndpy.add(y - Y[i])
    dpy = ndpy

if gy not in dpy:
    print('No')
    exit()

print('Yes')
