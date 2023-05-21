def max_sum(D, A, B):
    A.sort()
    B.sort()
    max_sum = -1

    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] >= B[j] and A[i] - B[j] <= D:
            max_sum = max(max_sum, A[i] + B[j])
            i += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1

    i = j = 0
    while i < len(A) and j < len(B):
        if B[j] >= A[i] and -(A[i] - B[j]) <= D:
            max_sum = max(max_sum, A[i] + B[j])
            j += 1
        elif B[j] < A[i]:
            j += 1
        else:
            i += 1

    i = M-1
    while 0 <= i:
        if abs(A[N-1] - B[i]) <= D:
            max_sum = max(max_sum, A[N-1] + B[i])
            i -= 1
        else:
            break

    i = N-1
    while 0 <= i:
        if abs(A[i] - B[M-1]) <= D:
            max_sum = max(max_sum, A[i] + B[M-1])
            i -= 1
        else:
            break

    return max_sum

# for testing
N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(max_sum(D, A, B))
