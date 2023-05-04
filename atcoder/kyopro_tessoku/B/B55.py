import bisect

A = []
Q = int(input())
for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        bisect.insort_left(A, int(query[1]))
    if query[0] == '2':
        if len(A) > 0:
            idx = bisect.bisect_left(A, int(query[1]))
            if idx < len(A):
                print(min(abs(A[idx] - int(query[1])), abs(A[idx - 1] - int(query[1]))))
            else:
                print(abs(A[idx - 1] - int(query[1])))
        else:
            print(-1)
