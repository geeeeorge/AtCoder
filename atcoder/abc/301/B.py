N = int(input())
A = list(map(int, input().split()))
ans = []

for i in range(len(A)-1):
    if A[i] < A[i+1]:
        while A[i] < A[i+1]:
            ans.append(A[i])
            A[i] += 1
    elif A[i] > A[i+1]:
        while A[i] > A[i+1]:
            ans.append(A[i])
            A[i] -= 1
ans.append(A[-1])
print(*ans)
