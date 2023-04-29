D, N = map(int, input().split())
R = [24] * D
for i in range(N):
    l, r, h = map(int, input().split())
    l -= 1
    r -= 1
    for i in range(l, r + 1):
        R[i] = min(R[i], h)
print(sum(R))
