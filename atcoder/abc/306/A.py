N = int(input())
S = input()
ans = ""
for i in range(N):
    ans += S[i] + S[i]
print(ans)
