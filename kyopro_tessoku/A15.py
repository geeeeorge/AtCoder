import bisect


N = int(input())
A = list(map(int, input().split()))

# XはAの要素を重複なく昇順に並べたもの
# Aの要素aがBの要素bで何になるかを表す
X = sorted(list(set(A)))
B = []

# 圧縮
for a in A:
    b = bisect.bisect(X, a)
    B.append(b)
print(*B)
