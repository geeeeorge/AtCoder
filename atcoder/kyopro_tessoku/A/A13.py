N, K = map(int, input().split())
A = list(map(int, input().split()))

# しゃくとり法
# Rにrightの最初の値を記録する
R = [0] * N

for left in range(N):
    if left > 0:
        R[left] = R[left - 1]
    while R[left] < N and A[R[left]] - A[left] <= K:
        R[left] += 1

ans = 0
for left in range(N):
    ans += R[left] - left - 1
print(ans)
