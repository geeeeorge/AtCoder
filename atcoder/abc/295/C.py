from collections import Counter
N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
ans = 0
for k, v in c.items():
    ans += v // 2
print(ans)
