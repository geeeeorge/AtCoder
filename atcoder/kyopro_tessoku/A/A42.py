N, K = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 0
for lo_a in range(101 - K):
    for lo_b in range(101 - K):
        cnt = 0
        for i in range(N):
            ok_a = False
            ok_b = False
            if lo_a <= A[i] <= lo_a + K:
                ok_a = True
            if lo_b <= B[i] <= lo_b + K:
                ok_b = True
            if ok_a and ok_b:
                cnt += 1
        ans = max(ans, cnt)

print(ans)

