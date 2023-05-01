N = int(input())
LR = []
for i in range(N):
    l, r = map(int, input().split())
    LR.append((l, r))

# 最終日が早い順に取ればよい
LR.sort(key=lambda x: x[1])

ans = 1
now = 0
for i in range(1, N):
    if LR[now][1] <= LR[i][0]:
        ans += 1
        now = i
print(ans)
