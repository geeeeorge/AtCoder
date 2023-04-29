A, B = map(int, input().split())

# 100の約数のリスト
divisor = [i for i in range(1, 101) if 100 % i == 0]
ans = False

for i in range(A, B + 1):
    if i in divisor:
        ans = True
        break

print('Yes' if ans else 'No')
