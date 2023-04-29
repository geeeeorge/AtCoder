N = int(input())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

# point: 順番とは限らない
for i in range(N+1):
    # 降順にする
    G[i].sort(reverse=True)

euler_tour = []
parent = [0] * (N+1)

# ビット反転で行きと帰りを区別する
stack = [~1, 1]

while stack:
    u = stack.pop()
    if u >= 0:  # 行き
        euler_tour.append(u)
        for v in G[u]:
            if v != parent[u]:
                parent[v] = u
                stack.append(~v)
                stack.append(v)
    else:  # 帰り
        euler_tour.append(parent[~u])

euler_tour.pop()
print(*euler_tour)
