class UnionFind:
    def __init__(self, n):
        import sys
        sys.setrecursionlimit(10 ** 6)

        self.parent = [-1] * n
        self.size = [1] * n

    def root(self, x: int) -> int:
        if self.parent[x] == -1:
            return x
        else:
            # 経路圧縮
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def merge(self, x: int, y: int) -> None:
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        # マージテク
        # xの方が大きい
        if self.size[x] < self.size[y]:
            x, y = y, x
        if self.size[x] == self.size[y]:
            self.size[x] += 1
        self.parent[y] = x

    def is_same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)


N, M = map(int, input().split())
A = []
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    A.append((a, b))
canceled = set(i for i in range(M))
cmd = []
Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]
for q in query:
    if q[0] == 1:
        q[1] -= 1
        canceled.discard(q[1])
    else:
        q[1] -= 1
        q[2] -= 1
    cmd.append(q)

uf = UnionFind(N)

for i in canceled:
    a, b = A[i]
    uf.merge(a, b)

ans = []
for c in reversed(cmd):
    if c[0] == 1:
        a, b = A[c[1]]
        uf.merge(a, b)
    else:
        ans.append("Yes" if uf.is_same(c[1], c[2]) else "No")
for a in reversed(ans):
    print(a)
