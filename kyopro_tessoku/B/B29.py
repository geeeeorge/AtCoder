A, B = map(int, input().split())
MOD = 10 ** 9 + 7


def mod_pow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res


print(mod_pow(A, B, MOD))
