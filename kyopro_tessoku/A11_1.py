import bisect

N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = bisect.bisect(A, X)
print(ans)