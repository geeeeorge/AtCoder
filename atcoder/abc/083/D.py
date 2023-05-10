S = input()

ans = len(S)
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        ans = min(ans, max(i, len(S)-i))
print(ans)
