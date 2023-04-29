N = int(input())
S = input()

dango = 0
kushi_list = [0]

for s in S:
    if s == 'o':
        dango += 1
    if s == '-':
        kushi_list.append(dango)
        dango = 0

dango = 0
for s in S[::-1]:
    if s == '-':
        kushi_list.append(dango)
        break
    if s == 'o':
        dango += 1

ans = max(kushi_list)
if ans == 0:
    print(-1)
else:
    print(ans)
