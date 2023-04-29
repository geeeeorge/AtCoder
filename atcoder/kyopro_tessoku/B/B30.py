H, W = map(int, input().split())
MOD = 10 ** 9 + 7


def pow(a, n, mod=10 ** 9 + 7):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res


def combination(n, r, m):
    # 分子aを求める
    a = 1
    for i in range(n):
        a = a * (i + 1) % m

    # 分母bを求める
    b = 1
    for i in range(r):
        b = b * (i + 1) % m
    for i in range(n - r):
        b = b * (i + 1) % m

    # bの逆元を求める
    b_inv = pow(b, m - 2, m)
    return a * b_inv % m


H -= 1
W -= 1
print(combination(H + W, H, MOD))
