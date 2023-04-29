N = int(input())
S = input()

# 右向きに見る
streak = 1
r = [1] * N
for i in range(N - 1):
    if S[i] == 'A':
        streak += 1
    else:
        streak = 1
    r[i + 1] = streak

# 左向きに見る
streak = 1
l = [1] * N
for i in range(N - 2, -1, -1):
    if S[i] == 'B':
        streak += 1
    else:
        streak = 1
    l[i] = streak

ans = []
for i in range(N):
    ans.append(max(r[i], l[i]))
print(sum(ans))
