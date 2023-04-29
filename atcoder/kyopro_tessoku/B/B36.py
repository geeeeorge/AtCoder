N, K = map(int, input().split())
S = input()
# 1の数を数える
cnt = 0
for i in range(N):
    if int(S[i]) == 1:
        cnt += 1

print('Yes' if K % 2 == cnt % 2 else 'No')
