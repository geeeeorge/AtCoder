def lcm(a, b):
    """
    最小公倍数を求める
    Least Common Multiple
    """
    def gcd(a, b):
        while a >= 1 and b >= 1:
            if a > b:
                a = a % b
            else:
                b = b % a
        return a if a != 0 else b

    return a * b // gcd(a, b)
