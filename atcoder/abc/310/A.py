N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

for i in range(N):
    D[i] += Q
D.append(P)

print(min(D))
