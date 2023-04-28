N, Q = map(int, input().split())
A = list(map(int, input().split()))

# 累積和を求めておく
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

for _ in range(Q):
    l, r = map(int, input().split())

    print(S[r] - S[l - 1])
