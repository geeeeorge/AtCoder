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


N, Q = map(int, input().split())
uf = UnionFind(N)
for _ in range(Q):
    cmd, u, v = map(int, input().split())
    if cmd == 1:
        uf.merge(u - 1, v - 1)
    else:
        if uf.is_same(u - 1, v - 1):
            print('Yes')
        else:
            print('No')
