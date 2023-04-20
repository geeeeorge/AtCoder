import heapq

Q = int(input())

# heapqで優先度付きキュー
# 要素の追加、削除はO(logN)
# 最小値の取得はO(1)
bag = []
heapq.heapify(bag)
addition = 0

for _ in range(Q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        heapq.heappush(bag, a[1] - addition)
    elif a[0] == 2:
        addition += a[1]
    else:
        print(heapq.heappop(bag) + addition)
