import bisect


N = int(input())
AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))

# ABをaでソート
AB.sort(key=lambda x: x[0])

# ABのbについてLIS
L = []
for i in range(N):
    pos = bisect.bisect_left(L, AB[i][1])
    if pos == len(L):
        L.append(AB[i][1])
    else:
        L[pos] = AB[i][1]
print(len(L))
