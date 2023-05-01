import heapq

N, D = map(int, input().split())
G = [[] for _ in range(2009)]
for i in range(N):
    x, y = map(int, input().split())
    G[x].append(y)

a = []
cnt = 0
ans = 0

for i in range(1, D + 1):
    for y in G[i]:
        heapq.heappush(a, -y)
    if a:
        ans -= heapq.heappop(a)

print(ans)

