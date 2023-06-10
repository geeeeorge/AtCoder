N, D = map(int, input().split())
X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

ans = ['No' for i in range(N)]
ans[0] = 'Yes'
mae = [0]

for _ in range(N):
    new_mae = []
    for j in mae:
        for i in range(N):
            if ans[i] == 'No':
                if (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2 <= D ** 2:
                    ans[i] = 'Yes'
                    new_mae.append(i)
    if len(new_mae) == 0:
        break
    mae = new_mae

for a in ans:
    print(a)
