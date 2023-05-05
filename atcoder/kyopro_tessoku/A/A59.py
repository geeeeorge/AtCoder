N, Q = map(int, input().split())

seg = [0] * (1 << 20)


# 一点更新
def update(k, x):
    k += 1 << 19
    seg[k] = x
    while k > 0:
        k //= 2
        seg[k] = seg[k * 2] + seg[k * 2 + 1]


# 区間取得
def get_sum(ql, qr, sl=0, sr=1 << 19, k=1):
    if qr <= sl or sr <= ql:
        return 0
    if ql <= sl and sr <= qr:
        return seg[k]
    m = (sl + sr) // 2
    return get_sum(ql, qr, sl, m, k * 2) + get_sum(ql, qr, m, sr, k * 2 + 1)


for _ in range(Q):
    cmds = list(map(int, input().split()))
    if cmds[0] == 1:
        pos, x = cmds[1:]
        update(pos, x)
    else:
        l, r = cmds[1:]
        print(get_sum(l, r))
