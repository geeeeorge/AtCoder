N, M = map(int, input().split())
A = list(map(int, input().split()))
minus_ans = [0] * N

for a in A:
    minus_ans[a-1] += 1

for i in range(N):
    print(M - minus_ans[i])
