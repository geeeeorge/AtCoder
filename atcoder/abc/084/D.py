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


is_prime = eratosthenes(10**5)
prime = set()
for i in range(10**5+1):
    if is_prime[i]:
        prime.add(i)

is_like2017 = [0] * (10**5+1)
for i in range(3, 10**5+1):
    if i in prime and (i + 1) / 2 in prime:
        is_like2017[i] = 1

# 累積和
for i in range(len(is_like2017)-1):
    is_like2017[i+1] += is_like2017[i]

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(is_like2017[r] - is_like2017[l-1])
