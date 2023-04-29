A, B = map(int, input().split())
MOD = 10 ** 9 + 7


def pow(a, n, mod=10 ** 9 + 7):
    """
    繰り返し二乗法
    """
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res


print(pow(A, B, MOD))
