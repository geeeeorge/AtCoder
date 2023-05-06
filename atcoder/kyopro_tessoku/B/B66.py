class UnionFind:
    """
    UnionFind
    """

    def __init__(self, n):
        import sys
        sys.setrecursionlimit(10 ** 6)

        self.parent = [-1] * n

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
        self.parent[x] = y

    def is_same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)


N, M = map(int, input().split())
A = []
B = []
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    A.append(a)
    B.append(b)
canceled = []
cmd = []
Q = int(input())
for _ in range(Q):
    q = list(map(int, input().split()))
    cmd.append(q)
    if q[0] == 1:
        canceled.append(q[1]-1)

uf = UnionFind(N)

for i in range(M):
    if i not in canceled:
        uf.merge(A[i], B[i])

ans = []
for _ in range(Q):
    c = cmd.pop()
    if c[0] == 1:
        uf.merge(A[c[1]-1], B[c[1]-1])
    else:
        if uf.is_same(c[1]-1, c[2]-1):
            ans.append('Yes')
        else:
            ans.append('No')
ans.reverse()
for a in ans:
    print(a)
