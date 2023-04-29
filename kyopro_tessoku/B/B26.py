N = int(input())


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


m = eratosthenes(N)
for i in range(N+1):
    if m[i]:
        print(i)
