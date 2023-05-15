from collections import Counter


S = input()
T = input()

l = [i for i in 'atcoder']


counter_S = Counter(S)
counter_T = Counter(T)
for i, v in counter_S.items():
    if i == '@':
        continue
    counter_T[i] -= v

cnt = 0
for i, v in counter_T.items():
    if i == '@':
        continue
    if i in l + ['@']:
        cnt += abs(v)
    if i not in l + ['@'] and v != 0:
        print('No')
        exit()
if cnt > counter_S['@'] + counter_T['@']:
    print('No')
    exit()

print('Yes')
