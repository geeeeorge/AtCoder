N, K = map(int, input().split())
R = list(map(int, input().split()))

R.sort()
C = 0

for i in range(K):
    C = (C + R[N-K+i]) / 2
print(C)
