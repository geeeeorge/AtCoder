S, T = input().split()

a = min(len(S), len(T))
f = False
for i in range(a):
    if S[i] < T[i]:
        print("Yes")
        f = True
        break
    elif S[i] > T[i]:
        print("No")
        f = True
        break

if not f:
    if len(S) < len(T):
        print("Yes")
    else:
        print("No")
