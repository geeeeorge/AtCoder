N, Q = map(int, input().split())
A = [i for i in range(1, N+1)]

reverse_flag = False
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if reverse_flag:
            A[N - query[1]] = query[2]
        else:
            A[query[1] - 1] = query[2]
    if query[0] == 2:
        reverse_flag = not reverse_flag
    if query[0] == 3:
        if reverse_flag:
            print(A[N - query[1]])
        else:
            print(A[query[1] - 1])
