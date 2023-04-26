N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L = []
R = []
for _ in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

# 累積和
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

for i in range(Q):
    win_num = S[R[i]] - S[L[i] - 1]
    lose_num = R[i] - L[i] + 1 - win_num
    if win_num > lose_num:
        print("win")
    elif win_num < lose_num:
        print("lose")
    else:
        print("draw")
