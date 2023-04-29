h, w = map(int, input().split())

l = []
for i in range(h):
    l.append(list(map(int, input().split())))

ret = [[0 for i in range(w)] for j in range(h)]

# 先に縦，横の合計を出しておく
vertical_sum_list = [sum([l[i][j] for i in range(h)]) for j in range(w)]
horizontal_sum_list = [sum([l[i][j] for j in range(w)]) for i in range(h)]

for i in range(h):
    for j in range(w):
        ret[i][j] = horizontal_sum_list[i] + vertical_sum_list[j] - l[i][j]

for i in range(h):
    print(*ret[i])