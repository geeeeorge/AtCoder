A, B = map(int, input().split())


def gcd(a, b):
    while a >= 1 and b >= 1:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a if a != 0 else b


def lcm(a, b):
    return a * b // gcd(a, b)


print(lcm(A, B))
