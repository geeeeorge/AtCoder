N = int(input())


def calc(x):
    return x ** 3 + x


left = 0
right = 100

while right - left > 1e-3:
    mid = (left + right) / 2
    if calc(mid) >= N:
        right = mid
    else:
        left = mid

print(left)
