A = list(map(int, input().split()))
base = 1
ans = 0
for i in range(len(A)):
    ans += A[i] * base
    base *= 2
print(ans)
