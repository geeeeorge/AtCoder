Q = int(input())
X = []
for _ in range(Q):
    x = int(input())
    X.append(x)


# エラトステネスの篩
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


m = eratosthenes(max(X))
for i in range(Q):
    if m[X[i]]:
        print('Yes')
    else:
        print('No')
