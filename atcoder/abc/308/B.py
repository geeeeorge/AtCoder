N, M = map(int, input().split())
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))

ans = 0
for i in range(len(C)):
    if C[i] not in D:
        p = P[0]
    else:
        p = P[D.index(C[i]) + 1]
    ans += p
print(ans)
