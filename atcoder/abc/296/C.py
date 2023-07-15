import copy


N, X = map(int, input().split())
A = list(map(int, input().split()))

B = copy.deepcopy(A)

for i in range(N):
    B[i] += X

A = set(A)
B = set(B)

print('Yes' if len(A.intersection(B)) != 0 else 'No')
