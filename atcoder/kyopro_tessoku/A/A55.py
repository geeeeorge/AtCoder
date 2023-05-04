import bisect

A = []
Q = int(input())
for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        bisect.insort_left(A, int(query[1]))
    if query[0] == '2':
        A.remove(int(query[1]))
    if query[0] == '3':
        idx = bisect.bisect_left(A, int(query[1]))
        if idx < len(A):
            print(A[idx])
        else:
            print(-1)
