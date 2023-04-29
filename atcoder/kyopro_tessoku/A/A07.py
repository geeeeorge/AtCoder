D = int(input())
N = int(input())

# r = Dの時ように配列を1つ多く取る
# 実際S[D]は使われない
S = [0] * (D + 1)
for i in range(N):
    l, r = map(int, input().split())
    S[l - 1] += 1
    S[r] -= 1

# いもす法
for i in range(1, D + 1):
    S[i] += S[i - 1]

for i in range(D):
    print(S[i])
