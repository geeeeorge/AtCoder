from collections import deque


N, M = map(int, input().split())
boxes = []

for i in range(M):
    k = int(input())
    boxes.append(deque(list((map(int, input().split())))))
for box in boxes:
    for i in range(len(box)):
        box[i] -= 1

# 一番上のカウンターを用意する
cnt = [[] for _ in range(N)]
q = deque()

# 初期のqueue作成
for i in range(M):
    cnt[boxes[i][0]].append(i)
for i in range(N):
    if len(cnt[i]) == 2:
        q.append(i)

while q:
    x = q.popleft()
    index1 = cnt[x][0]
    index2 = cnt[x][1]
    # cntを2から0に戻す
    cnt[x] = []
    # ボールを除去
    boxes[index1].popleft()
    boxes[index2].popleft()
    # cnt更新
    if len(boxes[index1]) != 0:
        cnt[boxes[index1][0]].append(index1)
        if len(cnt[boxes[index1][0]]) == 2:
            q.append(boxes[index1][0])
    if len(boxes[index2]) != 0:
        cnt[boxes[index2][0]].append(index2)
        if len(cnt[boxes[index2][0]]) == 2:
            q.append(boxes[index2][0])

# 結果出力
for box in boxes:
    if len(box) != 0:
        print("No")
        break
else:
    print("Yes")
