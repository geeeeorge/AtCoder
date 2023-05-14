N = int(input())
A = list(input())
B = list(input())

MOD = 998244353

for i in range(N):
    if A[i] <= B[i]:
        continue
    else:
        A[i], B[i] = B[i], A[i]

print((int(''.join(A)) % MOD) * (int(''.join(B)) % MOD) % MOD)
