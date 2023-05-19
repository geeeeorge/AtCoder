k = int(input())
a, b = input().split()

a10 = 0
b10 = 0

for i in range(len(a)):
    a10 *= k
    a10 += int(a[i])
for i in range(len(b)):
    b10 *= k
    b10 += int(b[i])
print(a10 * b10)
