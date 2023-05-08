from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)
for a in A:
    d[a] += 1

cnts = sorted(d.values(), reverse=True)
print(sum(cnts[K:]))

