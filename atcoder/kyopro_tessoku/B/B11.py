import bisect


N = int(input())
A = list(map(int, input().split()))
Q = int(input())
A.sort()

for _ in range(Q):
    x = int(input())
    ans = bisect.bisect_left(A, x)
    print(ans)
