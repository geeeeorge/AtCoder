N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# A>0, B>0の時
ans1 = 0
for i in range(N):
    if A[i] + B[i] > 0:
        ans1 += A[i] + B[i]

# A<0, B>0の時
ans2 = 0
for i in range(N):
    if - A[i] + B[i] > 0:
        ans2 += - A[i] + B[i]

# A>0, B<0の時
ans3 = 0
for i in range(N):
    if A[i] - B[i] > 0:
        ans3 += A[i] - B[i]

# A<0, B<0の時
ans4 = 0
for i in range(N):
    if - A[i] - B[i] > 0:
        ans4 += - A[i] - B[i]

print(max(ans1, ans2, ans3, ans4))
