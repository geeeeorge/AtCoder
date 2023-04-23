class UnionFind:
    def __init__(self, n):
        import sys
        sys.setrecursionlimit(10**6)

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


if __name__ == '__main__':
    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    uf = UnionFind(N)

    for _ in range(Q):
        p, a, b = map(int, input().split())
        # 隣接リスト作成
        G[a].append(b)
        G[b].append(a)

        # UnionFind
        if p == 0:
            uf.merge(a, b)
        else:
            if uf.is_same(a, b):
                print('Yes')
            else:
                print('No')
