N = input()

keta = 0
ans = 0

for i in range(len(N)):
    if N[len(N) - i - 1] == '1':
        ans += 2 ** keta
    keta += 1

print(ans)
