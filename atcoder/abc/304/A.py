N = int(input())
S, A = [], []
for i in range(N):
    s, a = map(str, input().split())
    S.append(s)
    A.append(int(a))

min_idx = A.index(min(A))

for i in range(min_idx, N):
    print(S[i])

for i in range(min_idx):
    print(S[i])
