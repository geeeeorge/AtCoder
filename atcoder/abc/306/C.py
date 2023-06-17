N = int(input())
A = list(map(int, input().split()))

cnt = [0] * N
pre_ans = [1] * N

for i, a in enumerate(A):
    cnt[a - 1] += 1
    if cnt[a - 1] == 2:
        pre_ans[a - 1] = i + 1
ans = []
for i, a in enumerate(pre_ans):
    ans.append((i + 1, a))
ans.sort(key=lambda x: x[1])
for a in ans:
    print(a[0], end=" ")
