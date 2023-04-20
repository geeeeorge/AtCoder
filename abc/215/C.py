import itertools

S, K = map(str, input().split())
K = int(K)

# 単純にpermutationsすると被るのでsetで一意に
a = set()
for v in itertools.permutations(S):
    a.add("".join(v))

b = list(a)
b.sort()

print(b[K-1])
