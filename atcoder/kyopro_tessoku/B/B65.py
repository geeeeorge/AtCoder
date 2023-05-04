from sys import setrecursionlimit

setrecursionlimit(10 ** 9)

N, T = map(int, input().split())
T -= 1

G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

rank = [0] * N
rank[T] = 1


def dfs(v, p):
    for to in G[v]:
        if to == p:
            continue
        dfs(to, v)
        rank[v] = max(rank[v], rank[to] + 1)


dfs(T, -1)
print(*rank)
