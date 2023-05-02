X, Y = map(int, input().split())

ans = []
# ユークリッドの互除法の逆
while not(X == 1 or Y == 1):
    if X < Y:
        c = Y // X
        for i in range(c):
            ans.append((X, Y))
            Y -= X
    else:
        c = X // Y
        for i in range(c):
            ans.append((X, Y))
            X -= Y

if X == 1:
    c = Y // X
    for i in range(c - 1):
        ans.append((X, Y))
        Y -= X
else:
    c = X // Y
    for i in range(c - 1):
        ans.append((X, Y))
        X -= Y

ans.reverse()

print(len(ans))
for i in range(len(ans)):
    print(*ans[i])
