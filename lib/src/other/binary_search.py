def binary_search(li, x):
    """
    二分探索
    """
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == x:
            return mid
        elif li[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
