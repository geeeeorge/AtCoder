N = int(input())
A = list(map(int, input().split()))

ans = False

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j or j == k or k == i:
                continue
            if (A[i] + A[j] + A[k]) == 1000:
                ans = True
                break

print("Yes" if ans else "No")
