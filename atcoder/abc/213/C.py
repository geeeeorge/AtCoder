H, W, N = map(int, input().split())

X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

# X, Yを座標圧縮する
Xdict = {x: i + 1 for i, x in enumerate(sorted(set(X)))}
Ydict = {y: i + 1 for i, y in enumerate(sorted(set(Y)))}

for i in range(N):
    print(Xdict[X[i]], Ydict[Y[i]])
