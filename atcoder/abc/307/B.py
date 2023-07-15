N = int(input())
S = []
for i in range(N):
    S.append(input())

flag = False
for i in range(N):
    for j in range(N):
        if i != j:
            s = S[i] + S[j]
            if s == s[::-1]:
                flag = True
                break
print('Yes' if flag else 'No')
