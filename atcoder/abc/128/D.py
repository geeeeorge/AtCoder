import heapq

N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0
for l in range(K+1):
    for r in range(K+1-l):
        if l + r > N:
            continue
        a = []
        for i in range(l):
            heapq.heappush(a, V[i])
        for j in range(r):
            heapq.heappush(a, V[len(V)-j-1])
        for k in range(K - l - r):
            if len(a) == 0:
                break
            if a[0] < 0:
                heapq.heappop(a)
        ans = max(ans, sum(a))
print(ans)
