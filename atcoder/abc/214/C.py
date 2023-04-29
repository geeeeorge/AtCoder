import copy

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

# n個宝石が存在する
# まず最初の候補は全てT_i
# 1から順に考えればよい
ans = copy.deepcopy(T)

for i in range(N-1):
    tmp = ans[i] + S[i]
    if tmp < ans[i+1]:
        ans[i+1] = tmp

# 最後だけ別で
tmp = ans[N-1] + S[N-1]
if tmp < ans[0]:
    ans[0] = tmp

for i in range(N-1):
    tmp = ans[i] + S[i]
    if tmp < ans[i+1]:
        ans[i+1] = tmp

# 最後だけ別で
tmp = ans[N-1] + S[N-1]
if tmp < ans[0]:
    ans[0] = tmp

print(*ans)