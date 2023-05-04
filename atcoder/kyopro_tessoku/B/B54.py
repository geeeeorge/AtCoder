from collections import defaultdict


N = int(input())
A = defaultdict(int)

for _ in range(N):
    A[int(input())] += 1

ans = 0
for k, v in A.items():
    if v >= 2:
        ans += v * (v - 1) // 2
print(ans)
