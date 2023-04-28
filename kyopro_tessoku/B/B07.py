T = int(input())
N = int(input())

S = [0] * (T + 1)
for i in range(N):
    l, r = map(int, input().split())
    S[l] += 1
    S[r] -= 1

for i in range(1, T):
    S[i] += S[i - 1]

for i in range(T):
    print(S[i])
