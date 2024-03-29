class UnionFind:
    """
    UnionFind
    """
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
