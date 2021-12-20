n = int(input())

class_1 = [0]
class_2 = [0]

for _ in range(n):
    c, p = map(int, input().split())
    if c == 1:
        class_1.append(p)
        class_2.append(0)
    if c == 2:
        class_1.append(0)
        class_2.append(p)

# 先に累積和をとる
for i in range(n):
    class_1[i+1] += class_1[i]
    class_2[i+1] += class_2[i]

q = int(input())

for _ in range(q):
    l, r = map(int, input().split())
    print(f'{class_1[r] - class_1[l-1]} {class_2[r] - class_2[l-1]}')
