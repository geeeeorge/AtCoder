N, X = map(int, input().split())
A = list(map(int, input().split()))

# AからXを二分探索する


def binary_search(l, x):
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = (left + right) // 2
        if l[mid] == x:
            return mid
        elif l[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


ans = binary_search(A, X)
print(ans+1)
