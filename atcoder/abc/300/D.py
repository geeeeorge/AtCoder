def eratosthenes(n):
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, n+1):
        # 既にFalseなら飛ばす
        if not(is_prime[i]):
            continue
        # √nまでで良い
        if i*i > n:
            break
        # iの倍数をFalseにする
        for k in range(i*2, n+1, i):
            is_prime[k] = False
    return is_prime


N = int(input())
P = []
is_prime = eratosthenes(3 * 10**5)
for i, p in enumerate(is_prime):
    if p:
        P.append(i)

cnt = 0
for ai in range(len(P)):
    # 枝刈り
    if P[ai] * P[ai] * P[ai + 1] * P[ai + 2] * P[ai + 2] > N:
        break
    for bi in range(ai+1, len(P)):
        # 枝刈り
        if P[ai] * P[ai] * P[bi] * P[bi + 1] * P[bi + 1] > N:
            break
        for ci in range(bi+1, len(P)):
            if P[ai] * P[ai] * P[bi] * P[ci] * P[ci] > N:
                break
            cnt += 1

print(cnt)
