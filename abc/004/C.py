N = int(input())

l = [i for i in range(1, 7)]

# 周期性があるので、Nを30で割った余りを求める
N %= 30

for i in range(N):
    index = i % 5
    l[index], l[index + 1] = l[index + 1], l[index]

print(*l, sep='')
