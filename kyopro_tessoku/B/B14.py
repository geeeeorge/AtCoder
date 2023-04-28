import bisect


N, K = map(int, input().split())
A = list(map(int, input().split()))

C, D = A[:N//2], A[N//2:]

# Cをbit全探索
set_C = set()
for bit1 in range(1 << len(C)):
    tmp = 0
    for i in range(len(C)):
        shift_i = 1 << i
        if bit1 & shift_i > 0:
            tmp += C[i]
    set_C.add(tmp)
l_C = list(set_C)
l_C.sort()

# Dをbit全探索
set_D = set()
for bit1 in range(1 << len(D)):
    tmp = 0
    for i in range(len(D)):
        shift_i = 1 << i
        if bit1 & shift_i > 0:
            tmp += D[i]
    set_D.add(tmp)
l_D = list(set_D)
l_D.sort()

# 二分探索
for c in l_C:
    idx = bisect.bisect(l_D, K - c)
    if l_D[idx - 1] == K - c:
        print("Yes")
        break
else:
    print("No")
