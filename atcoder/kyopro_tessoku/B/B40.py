n = int(input())

a = [0] * 109
b = list(map(int, input().split()))
for b in b:
    a[b % 100] += 1
ans = 0
for i in range(51):
    if i == 0:
        ans += a[0] * (a[0] - 1) // 2
    elif i == 50:
        ans += a[50] * (a[50] - 1) // 2
    else:
        ans += a[i] * a[100 - i]
print(ans)
