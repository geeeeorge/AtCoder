N = int(input())
C, S, F = [0], [0], [0]
for i in range(N - 1):
    c, s, f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)

for i in range(1, N+1):
    t = 0
    for j in range(i, N):
        # tがS[j]より小さいとき、S[j]に合わせる
        if t < S[j]:
            t = S[j]
        # tがF[j]の倍数でないとき、F[j]の倍数に合わせる
        if t % F[j] != 0:
            t += F[j] - t % F[j]
        t += C[j]
    print(t)
