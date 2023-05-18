S1 = input()
S2 = input()
S3 = input()
T = input()

ans = ''
for t in T:
    if t == '1':
        ans += S1
    if t == '2':
        ans += S2
    if t == '3':
        ans += S3
print(ans)