N = int(input())
A = list(input())
B = list(input())

if sorted(A) != sorted(B):
    print(-1)
    exit()

B.reverse()

# 後ろから順番に貪欲に見て行って、最大の部分列を構成
cur = 0
cnt = 0
while cur < N:
    a = A.pop()
    while True:
        if B[cur] != a:
            cur += 1
        else:
            cur += 1
            cnt += 1
            break
        if cur >= N:
            break
print(N - cnt)
