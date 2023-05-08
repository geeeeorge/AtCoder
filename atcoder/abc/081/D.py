N = int(input())
A = list(map(int, input().split()))

max_a = max(A)
min_a = min(A)

# 決定論的に決まる
print(2*N-1)
if abs(max_a) >= abs(min_a):
    max_index = A.index(max_a)
    for i in range(N):
        print(max_index+1, i+1)
    for i in range(N-1):
        print(i+1, i+2)
else:
    min_index = A.index(min_a)
    for i in range(N):
        print(min_index+1, i+1)
    for i in range(N, 1, -1):
        print(i, i-1)
