from itertools import product


N, M = map(int, input().split())
switches = []
for _ in range(M):
    switches.append(list(map(int, input().split())))
ps = list(map(int, input().split()))

cnt = 0
for bits in product([0, 1], repeat=N):
    flag = True
    for i in range(M):
        len_s = switches[i][0]
        on_num = 0
        for j in range(1, len_s+1):
            on_num += bits[switches[i][j]-1]
        if on_num % 2 != ps[i]:
            flag = False
            break
    if flag:
        cnt += 1
print(cnt)
