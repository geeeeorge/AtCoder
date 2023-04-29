N, K = map(int, input().split())
A = list(map(int, input().split()))

# 累積和
S = [0]
for i in range(N):
    S.append(S[i] + A[i])

# しゃくとり法
R = [0] * (N + 1)
for left in range(N + 1):
    if left > 0:
        R[left] = R[left - 1]
    while R[left] < (N + 1) and S[R[left]] - S[left] <= K:
        R[left] += 1

ans = 0
for left in range(N+1):
    ans += R[left] - left - 1
print(ans)
