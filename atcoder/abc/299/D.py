N = int(input())

left = 1
right = N


while left <= right:
    mid = (left + right) // 2
    print('?', mid)
    ans = int(input())
    if ans == 0:
        left = mid + 1
    elif ans == 1:
        right = mid - 1

if ans == 0:
    print('!', mid)
else:
    print('!', mid - 1)
