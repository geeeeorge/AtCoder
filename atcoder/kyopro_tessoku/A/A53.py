import heapq

Q = int(input())
A = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(A, query[1])
    elif query[0] == 2:
        print(A[0])
    else:
        heapq.heappop(A)
