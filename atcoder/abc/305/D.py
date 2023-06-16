import bisect


N = int(input())
A = list(map(int, input().split()))
Q = int(input())

B = [0] * ((N - 1) // 2)
for i in range((N - 1) // 2):
    B[i] = A[i * 2 + 2] - A[i * 2 + 1]

# Bは累積和をとる
# Bの最初に0を追加しておく
B = [0] + B
for i in range(1, (N - 1) // 2 + 1):
    B[i] += B[i - 1]

for q in range(Q):
    l, r = map(int, input().split())
    ans = 0

    idx_l = bisect.bisect_left(A, l)
    idx_r = bisect.bisect_right(A, r)

    if idx_l % 2 == 0:
        ans += A[idx_l] - l
    if idx_r % 2 == 0:
        ans += r - A[idx_r - 1]

    if idx_r % 2 == 0:
        ans += B[idx_r // 2 - 1]
    else:
        ans += B[idx_r // 2]

    ans -= B[idx_l // 2]
    print(ans)
