import bisect
import array

L, Q = map(int, input().split())

# bisect.insertではだめだった
# array.arrayだとinsertが速くて通る
head_list = array.array('i', [0, L])

for i in range(Q):
    q, x = map(int, input().split())
    # 二分探索
    index = bisect.bisect(head_list, x)
    if q == 1:
        head_list.insert(index, x)
    else:
        print(head_list[index] - head_list[index - 1])
