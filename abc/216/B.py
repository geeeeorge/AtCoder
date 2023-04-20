N = int(input())

name_list = set()
for _ in range(N):
    s, t = map(str, input().split())
    name_list.add(s + ' ' + t)

if len(name_list) == N:
    print('No')
else:
    print('Yes')
