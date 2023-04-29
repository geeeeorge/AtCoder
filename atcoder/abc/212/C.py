def min_abs_diff(a, b, n, m):
    a.sort()
    b.sort()

    min_abs = abs(A[0] - B[0])

    i = j = 0
    while i < n and j < m:
        diff = abs(a[i] - b[j])
        min_abs = min(min_abs, diff)

        if a[i] < b[j]:
            i += 1
        else:
            j += 1

    return min_abs


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(min_abs_diff(A, B, N, M))

