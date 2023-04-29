import sys
sys.setrecursionlimit(300000)

n = int(input())
adj_list = [[] for _ in range(n)]  # 都市間の道路の情報を格納する隣接リスト
for i in range(n - 1):
    a, b = map(int, input().split())
    if a != b:
        adj_list[a - 1].append(b - 1)
        adj_list[b - 1].append(a - 1)

# point: 順番とは限らない
for i in range(n):
    adj_list[i].sort()

visited = [False] * n  # 各都市が訪問されたかどうかを表すフラグ
visited[0] = True  # 都市1は最初に訪問されるため、フラグをTrueにする

ans_list = []


def dfs(city):
    global visited
    ans_list.append(city + 1)  # 都市番号は1-indexedであるため、1を加える
    if city == 0:
        f = [visited[q] for q in adj_list[0]]
        if all(f):
            return
    for next_city in adj_list[city]:
        if not visited[next_city]:
            visited[next_city] = True
            dfs(next_city)
            ans_list.append(city + 1)


dfs(0)
print(*ans_list)
