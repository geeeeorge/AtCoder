N, M = map(int, input().split())
A = list(map(int, input().split()))

P = set()


def divider(n):
    i = 2
    # nを割り切れるまでiを増やしていく
    while i * i <= n:
        if n % i == 0:
            P.add(i)
            while n % i == 0:
                n //= i
        i += 1
    # nが素数の場合
    if n != 1:
        P.add(n)


for a in A:
    print(P)
    divider(a)

print(P)
ans = [False, True] + [True] * (M - 1)

for p in P:
    # pの倍数をFalseにする
    for pn in range(p, M + 1, p):
        ans[pn] = False

print(sum(ans))
for i in range(1, M + 1):
    if ans[i]:
        print(i)
