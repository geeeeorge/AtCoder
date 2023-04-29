N = int(input())
s = 0

# pythonは大きい整数でも扱える
# ただし、TLEになるので注意
for _ in range(N):
    t, a = map(str, input().split())
    a = int(a)
    if t == '+':
        s += a
        s %= 10000
    elif t == '-':
        s -= a
        s %= 10000
    elif t == '*':
        s *= a
        s %= 10000
    if s < 0:
        s += 10000
    print(s)
