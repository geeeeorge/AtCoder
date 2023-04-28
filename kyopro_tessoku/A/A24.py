import bisect


N = int(input())
A = list(map(int, input().split()))

# LIS
L = []
for i in range(N):
    pos = bisect.bisect_left(L, A[i])

    # Lを更新
    if pos == len(L):
        L.append(A[i])
    else:
        L[pos] = A[i]

print(len(L))
