N, K = map(int, input().split())
A = list(map(int, input().split()))

min_A = min(A)

# 最大秒数
max_time = 10**9+1

# 二分探索
# 答えでニブタンする時はbisectが使えないのね


def check(time, l, n, k):
    sum = 0
    for i in range(N):
        sum += time // l[i]
    if sum < k:
        return False
    else:
        return True


left = 1
right = max_time
while left < right:
    mid = (left + right) // 2
    ans = check(mid, A, N, K)
    if ans:
        right = mid
    else:
        left = mid + 1

print(left)
